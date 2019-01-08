from calculation import *
from plotting import plot
from math import sin, e, sqrt
from .model import Model
from constants import g

# "initialLevel": Entry(self.top, font=font),
#             "alphaParam": Entry(self.top, font=font),
#             "outputArea": Entry(self.top, font=font),
#             "targetLevel": Entry(self.top, font=font),
#             "maxFlow": Entry(self.top, font=font)

class TwoSourcesModel(Model):

    def __init__(self, values: dict, input2, second):
        self.calcStruc = CalculationStructure()
        self.values = values
        self.input = input2
        self.second = second
        self.S = 10.0
        self.A = 2.0
        self.h = values['initialLevel']
        self.internalTime = 0.0

    def modelStep(self, time):
        delta = time - self.internalTime
        inlet = self.input(self.internalTime) + self.second(self.internalTime)
        # print(two)
        ratio = self.A / self.S
        out = ratio * sqrt(2 * g * self.h) * -1
        value =  delta * (out + (inlet / self.S)) + self.h
        # value = one + two
        
        if(value < 0.0):
            value = 0.0
        self.h = value
        self.internalTime = time
        return value
        

    def calculate(self):
        self.calcStruc.calculate(self.modelStep)

    def display(self):
        plot(self.calcStruc)

    
