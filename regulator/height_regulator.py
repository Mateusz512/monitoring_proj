from regulator import Regulator

class Height2StateRegulator(Regulator):
    def __init__(self, maxFlow):
        self.maxFlow = maxFlow
    
    def step(self, t, u, y):
        e = u -y 
        if(e > 0.0):
            return self.maxFlow
        else:
            return 0.0