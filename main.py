from math import cos
from model import SimpleCalculationStructure
from plotting import plot

cs = SimpleCalculationStructure()
cs.calculate(lambda x: cos(x))
plot(cs)

