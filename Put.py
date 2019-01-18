from GenetskiAlgoritam import Evoluitivni
from random import shuffle, random, randint

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

    def mutiraj(self, curentIter, allIter):
        # Koeficient na osnovu koga odlucujemo sta zelimo dalje da radimo
        koeficient = curentIter / allIter

        gradoviNova = self.gradovi[1:len(self.gradovi) - 1]
        # pola = len(gradoviNova)/2

        # Sta ti se vise svidja?

        # Nacin 1:Ovde dolazi malo do varijacija-funkcija nije linearna
        # mod = int(10 - 8*koeficient)
        # n = pola % mod

        # Nacin 2 :Linearna funkcija
        n = int(10 - 8 * koeficient)

        gradoviMutirana = []
        brojac = 0
        # Prvo ubacujem elemenat sa kraja,pa elem. sa pocetka...i tako u nekoliko iteracija u odnosu na koeficient.
        for i in range(n):
            gradoviMutirana.append(gradoviNova[len(gradoviNova) - 1 - i])
            gradoviMutirana.append(gradoviNova[i])
            brojac += 1  # bela brojac je uvek jednak sa n ovde
        # Zatim srednji deo liste koji nisam pipao,ubacujem na kraj liste,jedan po jedan
        for j in range(brojac, len(gradoviNova) - brojac):
            gradoviMutirana.append(gradoviNova[j])

        gradoviMutirana.append(self.gradovi[0])  # dodaj na kraj grad koji si izbacio
        gradoviMutirana.insert(0, self.gradovi[0])  # Dodaj na pocetak grad koji si izbacio
        self.gradovi = gradoviMutirana  # Postavi gradove na nove

        self.duzinaPuta = Put.izracunajPut(self.gradovi)


        #bela metod 2
        # idx1 = randint(1,len(self.gradovi) - 2)
        # idx2 = randint(1,len(self.gradovi) - 2)
        # self.gradovi[idx1], self.gradovi[idx2] = self.gradovi[idx2], self.gradovi[idx1]
        # self.duzinaPuta = Put.izracunajPut(self.gradovi)

        #bela metod 3
        # for i in range(30):
        #     idx1 = randint(1,len(self.gradovi) - 2)
        #     idx2 = randint(1,len(self.gradovi) - 2)
        #     self.gradovi[idx1], self.gradovi[idx2] = self.gradovi[idx2], self.gradovi[idx1]
        # self.duzinaPuta = Put.izracunajPut(self.gradovi)

    @staticmethod
    def napraviDete(parent1, parent2):
        p1 = parent1[0:-1]
        p2 = parent2[0:-1]
        child = []

        begin = randint(0, len(parent1)-1)
        end = randint(0, len(parent1)-1)
        if(begin > end):
            begin,end = end,begin
        middle = p2[begin:end]

        i = 0;
        idx = 0;
        try:
            while i < begin:
                if p1[idx] not in middle:
                    child.append(p1[idx])
                    i +=1
                idx += 1
        except:
            pass

        child.extend(middle)

        i = end
        while i < len(p1):
            if p1[idx] not in middle:
                child.append(p1[idx])
                i += 1
            idx += 1

        return child

    def ukrsti(self, partner):
        #
        # # Deca dobijena ukrstanjem.
        # dete1 = []
        # dete2 = []
        #
        # selfNova = self.gradovi[0:-1]  # Izbacujemo prvi
        # partnerNova = partner.gradovi[0:-1]  # Izbacujemo prvi
        #
        # cetvrtina = len(
        #     selfNova) // 4  # Ovo je indeks koji cu kasnije koristitit kako bi uradio ono sto smo pricali sa vukanom.
        #
        # dete1.extend(
        #     selfNova[cetvrtina:len(selfNova) - 1 - cetvrtina])  # Uzimamo pola prvog roditelja i ubacujemo u prvo dete
        # dete2.extend(partnerNova[cetvrtina:len(
        #     partnerNova) - 1 - cetvrtina])  # Uzimamo pola drugog roditelja i ubacujemo u drugo dete
        #
        # n = len(selfNova)
        #
        # for i in range(n):
        #     if (partnerNova[i] not in dete1):
        #         dete1.append(partnerNova[i])
        #     if (selfNova[i] not in dete2):
        #         dete2.append(selfNova[i])
        #
        # return (Put(dete1), Put(dete2))

        #bela metod 1
        # dete1 = Put.napraviDete(self.gradovi, partner.gradovi)
        # dete2 = Put.napraviDete(partner.gradovi, self.gradovi)
        # return (Put(dete1), Put(dete2))

        #bela metod 2
        del(self.gradovi[-1])
        del(partner.gradovi[-1])
        l = len(self.gradovi)
        dete1 = [None] * l
        dete2 = [None] * l


        begining = 0
        ending = 0
        while begining == ending:
            begining = randint(0,l-1)
            ending = randint(0,l-1)
        if(begining > ending):
            begining, ending = ending, begining

        midle1 = self.gradovi[begining:ending]
        midle2 = partner.gradovi[begining:ending]

        dete1[begining:ending] = midle1
        dete2[begining:ending] = midle2

        i1 = ending
        idx = 0
        while i1 != begining:
            if partner.gradovi[idx] not in midle1:
                dete1[i1] = partner.gradovi[idx]
                i1 += 1
                i1 %= l
            idx += 1


        i2 = ending
        idx = 0
        while i2 != begining:
            if self.gradovi[idx] not in midle2:
                dete2[i2] = self.gradovi[idx]
                i2 += 1
                i2 %= l
            idx += 1

        self.gradovi.append(self.gradovi[0])
        partner.gradovi.append(partner.gradovi[0])
        return (Put(dete1), Put(dete2))

    def getFitnes(self):
        return 1/self.duzinaPuta

    def __str__(self):
        s = ""
        for i in self.gradovi:
            s += " " + i.ime
        s += " " + str(self.duzinaPuta)
        return s

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