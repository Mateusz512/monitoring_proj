import numpy as np

class CalculationStructure:

    def __init__(self, end=100, step=0.01):
        self.step = step
        self.entriesCount = int(end / step)
        self.time = np.linspace(0, end, self.entriesCount)
        self.values = [(0,)] * self.entriesCount

    def calculate(self, func):
        self.values = list(map(func, self.time))

# On second thought... this way of doing this sucks, we will have to iterate right away
#
# class IntegrationCalculationStructure(SimpleCalculationStructure):
#
#     def integrate(self, tMinus, tNow, acc):
#         return (tMinus + tNow) / 2 * self.step + acc
#
#     def calculate(self, func):
#         for i in range(1, self.entriesCount):
#             self.values[i] = self.integrate(func(self.time[i - 1]), func(self.time[i]), self.values[i-1])
