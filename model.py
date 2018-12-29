import numpy


class SimpleCalculationStructure:

    def __init__(self, end=10, step=0.1):
        self.step = step
        self.entriesCount = int(end / step)
        self.time = numpy.linspace(0, end, self.entriesCount)
        self.values = [0] * self.entriesCount

    def calculate(self, func):
        self.values = list(map(func, self.time))


class IntegrationCalculationStructure(SimpleCalculationStructure):

    def integrate(self, tMinus, tNow):
        return (tMinus + tNow) / 2 * self.step

    def calculate(self, func):
        for i in range(1, self.entriesCount):
            self.values[i] = self.integrate(func(self.time[i - 1]), func(self.time[i]))
