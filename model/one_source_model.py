from calculation import *
from plotting import *
from math import sin, e, sqrt
from .model import Model
from constants import g
from regulator import Height2StateRegulator
            # "initialLevel": self.buildEntry("5.3", 812, 212, 132),
            # "outputDiameter": self.buildEntry("0.14", 296, 654, 96),
            # "tankDiameter": self.buildEntry("3", 296, 585, 96),
            # "targetLevel": self.buildEntry("10", 547, 47, 174),
            # "maxFlow": self.buildEntry("5.3", 34, 322, 155),
            # "maxLevel": self.buildEntry("25", 194, 459, 117)

class OneSourceModel(Model):

    def __init__(self, values: dict):
        self.calcStruc = CalculationStructure()
        self.values = values
        self.u = values['targetLevel']
        self.yMax = values['maxLevel']
        self.S = values['tankDiameter']
        self.A = values['outputDiameter']
        self.y = values['initialLevel']
        self.internalTime = 0.0
        self.regulator = Height2StateRegulator(self.values['maxFlow'])
        self.pc = PlotConfig([Label( "Czas [s]","Wysokość [m]", ""), Label("Czas [s]", "Przepływ [m3/s]", "")])

    def modelStep(self, time):
        if(time == self.internalTime) :
            return (self.y, 0.0)
        delta = time - self.internalTime
        sig = self.regulator.step(time, self.u, self.y)

        ratio = self.A / self.S
        out = ratio * sqrt(2 * g * self.y) * -1

        value =  delta * (out + (sig  / self.S)) + self.y
        
        if(value < 0.0):
            value = 0.0
        self.y = value
        self.internalTime = time
        return (value, sig)

    def calculate(self):
        self.calcStruc.calculate(self.modelStep)

    def display(self):
        plot(self.calcStruc, self.pc)

    
