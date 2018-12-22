from GenetskiAlgoritam import Evoluitivni
from random import shuffle

sviGradovi = {}

class Put(Evoluitivni):
    """klassa reprezentuje put prodavca
    atributi:
        gradovi-redosled gradova kako se posecaju
        duzinaPuta-duzina izabranog puta"""
    def __init__(self, gradovi):
        self.gradovi = gradovi.copy()
        self.gradovi.append(self.gradovi[0])
        self.duzinaPuta = Put.izracunajPut(self.gradovi)

    def getFitnes(self):
        return self.duzinaPuta

    def __str__(self):
        return "fitness = " + str(self.duzinaPuta)

    @staticmethod
    def randPut(gradovi):
        """vraca nasumicno izabran put
        input:
            gradovi-gradovi da se zaobidju
        output:
            Put-jedan nasumican put"""
        shuffle(gradovi)
        return Put(gradovi)

    @staticmethod
    def izracunajPut(nizGradova):
        """koristi se za izracunavanje duzine puta od niza gradova
        input:
            nizGradova-lista gradova od koji reprezentuje put prodavca
        output:
            zbir-duzina puta"""
        zbir = 0
        for i in range(len(nizGradova) - 1):
            zbir += nizGradova[i].udaljenost(nizGradova[i+1])
        return zbir

if __name__ == "__main__":
    pass