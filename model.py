import numpy


def integration(tMinus, tNow):
    return tNow


class SimpleCalculationStructure:

    def __init__(self, end=10, step=0.1):
        self.step = step
        self.entriesCount = int(end / step)
        self.time = numpy.linspace(0, end, self.entriesCount)
        self.values = [0] * self.entriesCount

    def calculate(self, func):
        self.values = list(map(func, self.time))


class IntegrationCalculationStructure(SimpleCalculationStructure):

    # def integrate(self, ):

    def calculate(self, func):
        for i in range(1, self.entriesCount):
            self.values[i] = integration(func(self.time[i - 1]), func(self.time[i]))