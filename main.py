from City import *
from  Road import *
from GeneticAlgorithm import *
import sys

if not len(sys.argv) == 2 :
    print("Usage: python main.py <file>")
    sys.exit(1)
fileName = sys.argv[1]
populationNum = 100
iterationNum = 10000


cities = {}
file = open(fileName, "r")
City.readFromFile(file, cities)
file.close()

roads = []
for i in range(populationNum):
    roads.append(Road.randRoad(list(cities.values())))

bestRoad = GA(roads, iterationNum)

print(bestRoad.roadDistance)

for city in bestRoad.cities:
    print(city)

print()

