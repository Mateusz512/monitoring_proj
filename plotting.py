import matplotlib.pyplot as plt
from model import SimpleCalculationStructure


def plot(*args: SimpleCalculationStructure):
    for cs in args:
        plt.plot(cs.time, cs.values)
    plt.show()
