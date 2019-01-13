from Grad import *
from  Put import *
from GenetskiAlgoritam import *

def proveri(p):
    for i in range(1,len(p.gradovi)):
        pronadjen = False
        for j in p.gradovi:
            if str(i) == j.ime:
                pronadjen = True
                break
        if pronadjen == False:
            return False
    return True


file = open("data_tsp.txt", "r")
Grad.ucitaljIzFile(file, sviGradovi)
file.close()

putevi = []
for i in range(9):
    putevi.append(Put.randPut(list(sviGradovi.values())))

for i in putevi:
    print(proveri(i))

m = GA(putevi, 1000)

print(m.duzinaPuta)

print(proveri(m))

print()