class Grad:
    """klassa reprezent grada
    atributi:
        ime-ime grada
        x-x kordinata
        y-y kordinata"""
    def __init__(self, linija):
        tokeni = linija.split(" ")
        self.ime = tokeni[0]
        self.x = float(tokeni[1])
        self.y = float(tokeni[2])

    def udaljenost(self, other):
        """koristi se za izracunavanje udaljenosti izmedju dva grada
        input:
            self
            other-drugi grad
        output:
            daljina-udaljenost izemdju dva grada"""
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5

    def __str__(self):
        """koristi se za stringovsku reprezentaciju grada
        input:
            self
        output:
            str-string reprezentacija grada"""
        return "ime = " + str(self.ime) + " x = " + str(self.x) + " y = " + str(self.y)

    @classmethod
    def ucitaljIzFile(cls, file, storage):
        """koristi se za ucitavanje svih gradova iz fajla
        input:
            file-file iz koga da se ucita
            storage-variabla u koju da se ucita
        output:
            none"""
        for linija in file:
            tacka = Grad(linija)
            storage[tacka.ime] = tacka


if __name__ == '__main__':
    ListaGradova = {}
    f = open("data_tsp.txt", 'r')
    Grad.ucitaljIzFile(f, ListaGradova)
    print(ListaGradova["1"])
    print(ListaGradova["2"])
    print(ListaGradova["1"].udaljenost(ListaGradova["2"]))
