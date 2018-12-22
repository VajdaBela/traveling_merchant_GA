from GenetskiAlgoritam import *
from random import random, randint

class Tacka(Evoluitivni):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        if x == 0 and y == 0:
            self.savrsenstvo = 1000000000000000000
        else:
            self.savrsenstvo = abs(1/(x**2 + y**2)**0.5)

    def __str__(self):
        return "x = " + str(self.x) + "y = " + str(self.y)

    def udaljenost(self, drugi):
        return ((self.x - drugi.x)**2 + (self.y - drugi.y)**2)**0.5

    def getFitnes(self):
        return self.savrsenstvo

    def ukrsti(self, partner):
        l = random()
        xo = (self.x + partner.x*l)/(1 + l)
        yo = (self.y + partner.y*l)/(1 + l)
        return (Tacka(xo, yo), Tacka(partner.x - xo, partner.y - yo))

    def mutiraj(self):
        if random() > 0.5:
            self.x + random()
            self.y + random()
        else:
            self.x - random()
            self.y - random()

if __name__ == "__main__":
    tacke = []
    for i in range(10):
        tacke.append(Tacka(randint(-100,100),randint(-100,100)))

    t = GA(tacke, 100)
    print(t.x, t.y)