from calculation import *
from plotting import plot
from math import sin, e, sqrt
from .model import Model
from constants import g
from regulator import HeightRegulator

class TwoSourcesModel(Model):

    def __init__(self, values: dict):
        self.calcStruc = CalculationStructure()
        self.values = values
        self.u = values['targetLevel']
        self.S = 10.0
        self.A = 2.0
        self.y = values['initialLevel']
        print("target: {}".format(self.u))
        print("init: {}".format(self.y))
        print("Flow: {}".format(self.values['maxFlow']))

        self.internalTime = 0.0
        # self.regulator = HeightRegulator(2.0, 4.0, 0.1, 0.6)
        self.rising = True

    def modelStep(self, time):
        # delta = time - self.internalTime
        # inlet = self.input(self.internalTime) + self.second(self.internalTime)
        # # print(two)
        # ratio = self.A / self.S
        # out = ratio * sqrt(2 * g * self.h) * -1
        # value =  delta * (out + (inlet / self.S)) + self.h
        # # value = one + two
        
        # if(value < 0.0):
        #     value = 0.0
        # self.h = value
        # self.internalTime = time
        # return value
        delta = time - self.internalTime
        e = self.u - self.y
        sig = self.regulate(e) / self.S
        # print("Signal: {}".format(sig))
        ratio = self.A / self.S
        out = ratio * sqrt(2 * g * self.y) * -1
        # print("Out: {}".format(out))

        value =  delta * (out + sig) + self.y
        # value = one + two
        
        if(value < 0.0):
            value = 0.0
        self.y = value
        self.internalTime = time
        return value
        
    def regulate(self, e):
        if(e > 0.0):
            return self.values['maxFlow']
        else:
            return 0.0

    def calculate(self):
        self.calcStruc.calculate(self.modelStep)

    def display(self):
        plot(self.calcStruc)

    
