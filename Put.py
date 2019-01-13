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

    def mutiraj(self, curentIter, allIter):
        #Koeficient na osnovu koga odlucujemo sta zelimo dalje da radimo
        koeficient = curentIter / allIter 

        gradoviNova = self.gradovi[1:len(self.gradovi)-1]
        #pola = len(gradoviNova)/2

        #Sta ti se vise svidja?

        #Nacin 1:Ovde dolazi malo do varijacija-funkcija nije linearna
        #mod = int(10 - 8*koeficient)
        #n = pola % mod
        
        #Nacin 2 :Linearna funkcija
        n = int(10 - 8*koeficient)

        gradoviMutirana = []
        brojac = 0
        #Prvo ubacujem elemenat sa kraja,pa elem. sa pocetka...i tako u nekoliko iteracija u odnosu na koeficient.
        for i in range(n):
            
            gradoviMutirana.append(gradoviNova[len(gradoviNova)-1-i]) 
            gradoviMutirana.append(gradoviNova[i])
            brojac += 1 #bela brojac je uvek jednak sa n ovde
        #Zatim srednji deo liste koji nisam pipao,ubacujem na kraj liste,jedan po jedan
        for j in range(brojac , len(gradoviNova)-brojac):
            gradoviMutirana.append(gradoviNova[j])

        gradoviMutirana.append(self.gradovi[0])#dodaj na kraj grad koji si izbacio
        gradoviMutirana.insert(0 ,self.gradovi[0] )#Dodaj na pocetak grad koji si izbacio
        self.gradovi = gradoviMutirana#Postavi gradove na nove

    def ukrsti(self, partner):
        
        
        
        #Deca dobijena ukrstanjem.
        dete1 = []
        dete2 = []
        
        self.selfNova = self.gradovi[1:len(self.gradovi)-1]#Izbacujemo prvi i poslednji
        self.partnerNova = partner.gradovi[1:len(self.gradovi)-1]#Izbacujemo prvi i poslednji
        
        cetvrtina = int(len(self.selfNova)/4) #Ovo je indeks koji cu kasnije koristitit kako bi uradio ono sto smo pricali sa vukanom.

        
        dete1.extend(self.selfNova[cetvrtina:len(self.selfNova)-1-cetvrtina])#Uzimamo pola prvog roditelja i ubacujemo u prvo dete
        dete2.extend(self.partnerNova[cetvrtina:len(self.partnerNova)-1-cetvrtina])#Uzimamo pola drugog roditelja i ubacujemo u drugo dete
        
        n = len(self.selfNova)

        try:
            for i in range(n):
                if(self.partnerNova[i] not in dete1):
                    dete1.append(self.partnerNova[i])
        except IndexError:

            for m in enumerate(self.partnerNova):
                print(m[0], m[1].ime)
            g = self.partnerNova[0]
            if(g not in self.gradovi):
                print("e")
            pass


        for j in range(n):
            if(self.selfNova[j] not in dete2):
                dete2.append(self.selfNova[j])

        dete1.append(self.gradovi[len(self.gradovi)-1])
        dete1.insert(0 ,self.gradovi[0] )

        dete2.append(self.gradovi[len(self.gradovi)-1])
        dete2.insert(0 ,self.gradovi[0] )

        self.gradovi = dete1
        partner.gradovi = dete2
        
        return ( self, partner)

    def getFitnes(self):
        return 1/self.duzinaPuta

    def __str__(self):
        return "fitness = " + str(self.getFitnes())

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