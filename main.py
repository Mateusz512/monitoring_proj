from model import SimpleCalculationStructure, IntegrationCalculationStructure
from plotting import plot

cs = SimpleCalculationStructure()
cs.calculate(lambda x: x)
cs2 = IntegrationCalculationStructure()
cs2.calculate(lambda x: x)
plot(cs, cs2)

