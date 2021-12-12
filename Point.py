from GeneticAlgorithm import Evolvable, GA
from random import random, randint
import math

#class for testing. Implemented more easily than Put
class Tacka(Evolvable):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        if x == 0 and y == 0:
            self.fitness = math.inf
        else:
            self.fitness = 1/math.sqrt(x**2 + y**2)

    def __str__(self):
        return "x = " + str(self.x) + "y = " + str(self.y)

    def getFitness(self):
        return self.fitness

    def crossbreed(self, partner):
        l = random()
        xo = (self.x + partner.x*l)/(1 + l)
        yo = (self.y + partner.y*l)/(1 + l)
        return (Tacka(xo, yo), Tacka(partner.x - xo, partner.y - yo))

    def printInfo(self):
        print(self)

    def mutate(self, currentIter, allIter):
        if random() > 0.5:
            self.x + random()
            self.y + random()
        else:
            self.x - random()
            self.y - random()

if __name__ == "__main__":
    points = []
    for i in range(10):
        points.append(Tacka(randint(-100,100),randint(-100,100)))

    t = GA(points, 100)
    print(t.x, t.y)
