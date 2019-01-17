from calculation import *
from plotting import plot
from math import sin, e, sqrt
from .model import Model
from constants import g
from regulator import ConcentrationRegulator
from plotting import Label, PlotConfig

class TwoSourcesModel(Model):

    def __init__(self, values):
        self.calcStruc = CalculationStructure()
        self.inA = values['maxFlowA']
        self.ratioA = values['ratioA']
        self.inB = values['maxFlowB']
        self.ratioB = values['ratioB']
        self.u = values['targetRatio']
        self.hMax = values['maxLevel']
        self.h = values['initialLevel']
        self.ratio = values['initialRatio']
        self.S = values['tankDiameter']
        self.A = values['outputDiameter']
        self.internalTime = 0.0
        self.regulator = ConcentrationRegulator(self.inA, self.inB, self.ratioA, self.ratioB)
        self.pc = PlotConfig([Label("czas [s]", "Stężenie [%]", ""), Label("czas [s]", "Wysokość [m]", ""), Label("Czas [s]", "FlowA [m3/s]", ""), Label("Czas [s]", "FlowB [m3/2]", "")])

    def modelStep(self, time):
        if(time == self.internalTime):
            return (self.ratio, self.h, 0.0, 0.0)
        delta = time - self.internalTime
        # inlet = self.input(self.internalTime) + self.second(self.internalTime)
        a, b = self.regulator.step(time, self.u, self.ratio)
        
        inlet = (a + b)
        if(self.h + (inlet * delta) > self.hMax):
            inlet = 0.0
            a = 0.0
            b = 0.0
        else:
            inletRatio = (a * self.ratioA + b * self.ratioB) / inlet
            self.ratio = ((self.h * self.S * self.ratio) + (inlet * inletRatio)) / ((self.h * self.S) + inlet)
       
        # # print(two)
        delimeterRation = self.A / self.S
        out = delimeterRation * sqrt(2 * g * self.h) * -1
        value =  delta * (out + (inlet / self.S)) + self.h
        # # value = one + two
        
        if(value < 0.0):
            value = 0.0
        if(self.ratio < 0.0):
           self.ratio = 0.0
        self.h = value
        self.internalTime = time
        return (self.ratio, self.h, a, b)


    def calculate(self):
        self.calcStruc.calculate(self.modelStep)

    def display(self):
        plot(self.calcStruc, self.pc)
