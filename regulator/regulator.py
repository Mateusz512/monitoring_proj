from abc import ABC, abstractmethod

class Regulator(ABC):
    @abstractmethod
    def step(self, time, t, u, y):
        pass