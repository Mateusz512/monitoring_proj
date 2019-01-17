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
        targetRatio = u + e
        if(targetRatio < 0.0):
            targetRatio = 0.0
        aToBRatio = abs(targetRatio - self.con2)/abs(self.con1 - targetRatio)

        aflow = self.max2 * aToBRatio
        bflow = self.max2
        if(aflow > self.max1):
            bflow = bflow * (self.max1 / aflow)
            aflow = self.max1
        if(bflow > self.max2):
            aflow = aflow * (self.max2 / bflow)
            bflow = self.max2
        return (aflow, bflow)

        # if(e > 0):
        #     if(self.con1 > self.con2):
        #         return (self.max1, 0.0)
        #     else:
        #         return (0.0, self.max2)
        # else:
        #     if(self.con1 < self.con2):
        #         return (self.max1, 0.0)
        #     else:
        #         return (0.0, self.max2)
        
        


