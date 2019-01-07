from calculation import *
from plotting import plot
from math import sin, e


class TwoSourcesModel:

    def __init__(self, values: dict, input):
        self.calcStruc = CalculationStructure()
        self.values = values
        self.input = input
        self.x = 0.0
        self.y = 0.0
        self.T = 3.0
        self.internalTime = 0.0

    def modelStep(self, time):
        delta = time - self.internalTime
        T = 1.0 / self.T
        value = T * delta * (self.input(self.internalTime) - self.y) + self.y
        self.y = value
        self.internalTime = time
        return value

        

    def calculate(self):
        self.calcStruc.calculate(self.modelStep)

    def display(self):
        plot(self.calcStruc)

    
