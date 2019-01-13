from Grad import *
from  Put import *
from GenetskiAlgoritam import *

file = open("data_tsp.txt", "r")
Grad.ucitaljIzFile(file, sviGradovi)
file.close()

putevi = []
for i in range(9):
    putevi.append(Put.randPut(list(sviGradovi.values())))

m = GA(putevi, 100000)

print(m.duzinaPuta)

print()