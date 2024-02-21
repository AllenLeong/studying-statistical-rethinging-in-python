from functools import reduce
import numpy as np

def factorial(x):
    if x in [0,1]:
        return 1
    return reduce(lambda x,y: x*y, [i for i in range(1,x+1)])

class Binominal:
    def __init__(self, prob: float= None, trails: int = None):
        self.prob = prob
        self.trails = trails
        pass

    def probability(self, x):
        p = factorial(self.trails)/(factorial(self.trails-x)*factorial(x))
        p *= (self.prob**x * (1-self.prob)**(self.trails - x))

        return p