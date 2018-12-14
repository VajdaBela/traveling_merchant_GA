sviGradovi = {}

class Put:

    def __init__(self, gradovi):
        self.gradovi = gradovi
        self.duzinaPuta = Put.izracunajPut(self.gradovi)


    @staticmethod
    def izracunajPut(nizGradova):
        zbir = 0
        for i in range(len(nizGradova) - 1):
            zbir = nizGradova[i].udaljenost(nizGradova[i+1])
        return zbir