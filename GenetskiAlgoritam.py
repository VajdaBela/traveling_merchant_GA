import random

sansa_mutiranja = 0.1
jacinaTurnamenta = 5

class Evoluitivni:
    """interface za sve klase koji zele da koriste GA"""
    def mutiraj(self, curentIter, allIter):
        """koristi se za mutiranje jedinke
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

    def getFitnes(self):
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

    n = len(roditelji)
    d = []
    izabrani = []
    for i in range(n//jacinaTurnamenta):
        while True:
            l = random.randint(0, n-1)
            if l not in izabrani:
                izabrani.append(l)
                break
        d.append(roditelji[l])

    for i in range(2):
        for j in range(i+1,len(d)):
            if d[j].getFitnes() > d[i].getFitnes():
                d[j], d[i] = d[i], d[j]

    return (d[0], d[1])

def nadji(populacija, tip="najgori"):
    """pronalazi najgori ili najbolji u populaciji
    input:
        populacija-populacija u kom se trazi
        tip-da trazi najgorag ili najboljeg
    output:
        najgoriIdx-index na kom se nalazi trazena jedinka"""
    najgoriIdx = 0
    if tip == "najgori":
        for i in range(len(populacija)):
            if populacija[i].getFitnes() < populacija[najgoriIdx].getFitnes():
                najgoriIdx = i
        return najgoriIdx
    else:
        for i in range(len(populacija)):
            if populacija[i].getFitnes() > populacija[najgoriIdx].getFitnes():
                najgoriIdx = i
        return najgoriIdx

def GA(roditelji, brIteracija):
    """Genetski algoritam
    input:
        roditelji-pocetni skup roditelja, mora biti paran broj roditelja
        brIteracija-broj generacija koje ce se generisati
    output:
        najbolji-najbolja pronadjena jedinka"""

    brPopulacije = len(roditelji)
    i = 0
    while i < brIteracija:
        deca = []
        for n in range(brPopulacije//2):
            otac ,majka = izaberiRoditelja(roditelji)
            (dete1,dete2) = otac.ukrsti(majka)
            if(random.random() < sansa_mutiranja):
                dete1.mutiraj(i,brIteracija)
                dete2.mutiraj(i,brIteracija)
            deca.append(dete1)
            deca.append(dete2)
        najboljiRoditeljIdx = nadji(roditelji, "najbolji")
        najgoreDeteIdx = nadji(deca)
        deca[najgoreDeteIdx] = roditelji[najboljiRoditeljIdx]
        print(i,roditelji[najboljiRoditeljIdx].duzinaPuta)
        roditelji = deca
        i += 1

    return roditelji[nadji(roditelji, "najbolji")]

