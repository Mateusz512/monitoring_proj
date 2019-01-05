from calculation import *
from plotting import plot


class Model:

    def __init__(self, values: dict):
        self.calcStruc = CalculationStructure()
        self.values = values

    def calculate(self):
        self.calcStruc.calculate(
            lambda x:
            # TODO: have fun @worekleszczy
            x)

    def display(self):
        plot(self.calcStruc)
