from GenetskiAlgoritam import Evoluitivni

sviGradovi = {}

class Put(Evoluitivni):
    """klassa reprezentuje put prodavca
    atributi:
        gradovi-redosled gradova kako se posecaju
        duzinaPuta-duzina izabranog puta"""
    def __init__(self, gradovi):
        self.gradovi = gradovi
        self.duzinaPuta = Put.izracunajPut(self.gradovi)


    @staticmethod
    def izracunajPut(nizGradova):
        """koristi se za izracunavanje duzine puta od niza gradova
        input:
            nizGradova-lista gradova od koji reprezentuje put prodavca
        output:
            zbir-duzina puta"""
        zbir = 0
        for i in range(len(nizGradova) - 1):
            zbir = nizGradova[i].udaljenost(nizGradova[i+1])
        return zbir

if __name__ == "__main__":
    pass