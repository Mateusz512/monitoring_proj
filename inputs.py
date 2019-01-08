def step(k):
    def stepFnc(time):
        if(time < 0.0):
            return 0.0
        else:
            return k
    return stepFnc

def delay(k, t):
    def delayFnc(time):
        if(time < t):
            return 0.0
        else:
            return k
    return delayFnc

def stepDown(k, t):
    def stepDownFnc(time):
        if(time < t):
            return k
        else:
            return 0.0
    return stepDownFnc

def combine(f1, f2):
    def combineFnc(time):
        return f1(time) + f2(time)
    return combineFnc