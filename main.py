from Grad import *
from  Put import *
from GenetskiAlgoritam import *

fileName = "data_tsp.txt"
br_populacija = 100
br_iteracija = 10000


file = open(fileName, "r")
Grad.ucitaljIzFile(file, sviGradovi)
file.close()

putevi = []
for i in range(br_populacija):
    putevi.append(Put.randPut(list(sviGradovi.values())))

m = GA(putevi, br_iteracija)

print(m.duzinaPuta)

for g in m.gradovi:
    print(g)

print()