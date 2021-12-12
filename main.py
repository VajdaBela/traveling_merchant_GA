from Grad import *
from  Put import *
from GenetskiAlgoritam import *
import sys

fileName = "data_tsp.txt"
populationNum = 100
iterationNum = 10000


cities = {}
file = open(fileName, "r")
Grad.readFromFile(file, cities)
file.close()

roads = []
for i in range(populationNum):
    roads.append(Put.randPut(list(cities.values())))

bestRoad = GA(roads, iterationNum)

print(bestRoad.roadDistance)

for city in bestRoad.cities:
    print(city)

print()

