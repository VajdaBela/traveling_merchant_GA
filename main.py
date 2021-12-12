from City import *
from  Road import *
from GeneticAlgorithm import *
import sys

fileName = "data_tsp.txt"
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

