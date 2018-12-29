import matplotlib.pyplot as plt
from model import SimpleCalculationStructure


def plot(cs: SimpleCalculationStructure):
    plt.plot(cs.time, cs.values)
    plt.show()
