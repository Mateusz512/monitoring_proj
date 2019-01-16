import matplotlib.pyplot as plt

from calculation import CalculationStructure

class Label:
    def __init__(self, xLabel = "value", yLable = "unit", title = "what a surprise"):
        self.xLabel = xLabel
        self.yLabel = yLable
        self.title = title


class PlotConfig:

    def __init__(self, labels: list):
        self.vectorSize = len(labels)
        self.labels = labels


def plot(cs: CalculationStructure, config: PlotConfig):
    values = list(zip(*cs.values))
    for i in range(config.vectorSize):
        label = config.labels[i]
        plt.figure(i)
        plt.plot(cs.time, values[i])
        plt.xlabel(label.xLabel)
        plt.ylabel(label.yLabel)
        plt.title(label.title)
    plt.show()

    # for cs in args:
    #     plt.plot(cs.time, cs.values)
    # plt.xlabel(config.xLabel)
    # plt.ylabel(config.yLabel)
    # plt.title(config.title)
    # plt.show()
    # print("nice plot")
