import random

class Evoluitivni:
    """interface za sve klase koji zele da koriste GA"""
    def mutiraj(self):
        """koristi se za mutiranje jedinku
        input:
            self
        output:
            self"""
        raise NotImplementedError(self.__class__ + ": mutiraj nije implementiran")

    def ukrsti(self, partner):
        """koristi se za ukrstanje jedinki
        input:
            self
            partner-istog tipa kao self,jedan u paru koji cini potomke
        output:
            deca-dvoclana lista koja sadrzi dva potomka"""
        raise NotImplementedError(self.__class__ + ": ukrsti nije implementiran")

    def getFtines(self):
        """koristi se za procenu dobrote jedinke
        input:
            self
        output:
            fitnes-realni broj, obelezava nivo savrsenstva"""
        raise NotImplementedError(self.__class__ + ": getFitness nije implementiran")


def izaberiRoditelja(roditelji):
    """vraca jednog roditelja, najvece sanse imaju da budu izabrani sa najvecim fitnesom
    input:
        roditelji-lista mogucih kandidata da budu roditelji
    output:
        roditelj-izabrani roditelj"""
    fitnesZbir = 0
    for roditelj in roditelji:
        fitnesZbir += roditelj.getFitnes()

    r = random.random()

    for roditelj in roditelji:
        r -= roditelj.getFitnes() / fitnesZbir
        if r <= 0:
            return roditelj
    return roditelji[-1]


def GA(roditelji, brIteracija):
    """Genetski algoritam
    input:
        roditelji-pocetni skup roditelja, mora biti paran broj roditelja
        brIteracija-broj generacija koje ce se generisati
    output:
        najbolji-najbolja pronadjena jedinka"""
    i = 0
    while i < brIteracija:
        otac = izaberiRoditelja(roditelji)
        majka = izaberiRoditelja(roditelji)
        i += 1

