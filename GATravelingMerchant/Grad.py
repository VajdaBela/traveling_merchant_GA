class Grad:
    'grad je obelezen sa x i y kordinatom'
    def __init__(self, linija):
        tokeni = linija.split(" ")
        self.ime = tokeni[0]
        self.x = float(tokeni[1])
        self.y = float(tokeni[2])

    def udaljenost(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5

    def __str__(self):
        return "ime = " + self.ime + " x = " + self.x + " y = " + self.y

    @classmethod
    def ucitaljIzFile(cls, file, storage):
        for linija in file:
            tacka = Grad(linija)
            storage[tacka.ime] = tacka


if __name__ == '__main__':
    ListaGradova = {}
    f = open("data_tsp.txt", 'r')
    Grad.ucitaljIzFile(f, ListaGradova)
    print()