from Grad import *
from  Put import *
from GenetskiAlgoritam import *

def proveri(p):
    for i in sviGradovi.values():
        if i not in p.gradovi:
            return False
    return True



file = open("data_tsp.txt", "r")
Grad.ucitaljIzFile(file, sviGradovi)
file.close()

putevi = []
for i in range(9):
    putevi.append(Put.randPut(list(sviGradovi.values())))

m = GA(putevi, 10000)

print(m.duzinaPuta)

for g in m.gradovi:
    print(g)

print()