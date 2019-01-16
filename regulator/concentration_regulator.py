from regulator import Regulator

class ConcentrationRegulator(Regulator):
    def __init__(self, max1, max2, con1, con2):
        self.max1 = max1
        self.max2 = max2
        self.con1 = con1
        self.con2 = con2

    def step(self, t, u, y):
        # if(u > max(self.con1, self.con2) or u < min(self.con2, self.con1)):
        #     raise ValueError("Inavlid target concentration")
        #error
        e = u - y
        if(e > 0):
            if(self.con1 > self.con2):
                return (self.max1, 0.0)
            else:
                return (0.0, self.max2)
        else:
            if(self.con1 < self.con2):
                return (self.max1, 0.0)
            else:
                return (0.0, self.max2)
        
        


