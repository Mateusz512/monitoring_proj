import matplotlib.pyplot as plt

from model import SimpleCalculationStructure


class PlotConfig:

    def __init__(self, xLabel="Czas [s]", yLabel="poziom cieczy [l]"):
        self.xLabel = xLabel
        self.yLabel = yLabel


def plot(*args: SimpleCalculationStructure, config: PlotConfig = PlotConfig()):
    for cs in args:
        plt.plot(cs.time, cs.values)
    plt.xlabel(config.xLabel)
    plt.ylabel(config.yLabel)
    plt.show()
