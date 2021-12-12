from GeneticAlgorithm import Evolvable
from random import shuffle, random, randint


class Road(Evolvable):
    """
    this class represents the road of a salesperson
    attributes:
        cities - the order in which the cities should be visited
        roadDistance - distance of the current road
    """
    def __init__(self, cities):
        self.cities = cities.copy()
        self.cities.append(self.cities[0])
        self.roadDistance = Road.calculateDistance(self.cities)

    def mutate(self, currentIter, allIter):
        """
        see Evolvable
        """
        #reshuffleNum number of cities will be reshuffled
        #atmost 10 will be reshufled, this happens in the beginning of GA
        #atminimum 2 will be reshufled, this happens as the GA is nearing the end 
        reshuffleNum = int(10 - 8 * currentIter / allIter)

        #last city is removed because it is the same as the first one
        self.cities.pop()

        #reshuufling by taking a city from the end, and then from the beginning
        newRoad = []
        for i in range(reshuffleNum):
            newRoad.append(self.cities[-i-1])
            newRoad.append(self.cities[i])

        #add remaining cities
        newRoad.extend(self.cities[reshuffleNum:-reshuffleNum])

        newRoad.append(newRoad[0]) #make road a circle again
        self.cities = newRoad
        self.roadDistance = Road.calculateDistance(self.cities) #recalculate length of road


    def crossbreed(self, partner):
        """
        To make the first child first take out the middle of self, and pad out the sides from partner.
        Inverse is true for the second child
        see Evovable
        """
        #remove repeated city
        self.cities.pop()
        partner.cities.pop()
        roadLen = len(self.cities)
        child1 = [None] * roadLen
        child2 = [None] * roadLen

        #get beginning and end idx of middle
        beginning = 0
        ending = 0
        while beginning == ending:
            beginning = randint(0,roadLen-1)
            ending = randint(0,roadLen-1)
        if(beginning > ending):
            beginning, ending = ending, beginning

        #get middle of partner and self
        selfMidle = self.cities[beginning:ending]
        partnerMidle = partner.cities[beginning:ending]

        child1[beginning:ending] = selfMidle
        child2[beginning:ending] = partnerMidle

        #child cities are added from ending, loops around to beginning and continues to beginning
        child1Idx = ending
        child2Idx = ending
        for parentIdx in range(0, roadLen):
            if partner.cities[parentIdx] not in selfMidle:
                child1[child1Idx] = partner.cities[parentIdx]
                child1Idx += 1
                child1Idx %= roadLen
            if self.cities[parentIdx] not in partnerMidle:
                child2[child2Idx] = self.cities[parentIdx]
                child2Idx += 1
                child2Idx %= roadLen

        #return removed cities
        self.cities.append(self.cities[0])
        partner.cities.append(partner.cities[0])

        return (Road(child1), Road(child2))

    def printInfo(self):
        """
        see Evolvable
        """
        print(self.roadDistance)

    def getFitness(self):
        """
        see Evolvabel
        """
        return 1/self.roadDistance

    def __str__(self):
        s = ""
        for i in self.cities:
            s += " " + i.name
        s += " " + str(self.roadDistance)
        return s

    @staticmethod
    def randRoad(cities):
        """
        makes random road
        input:
            cities - cities to be visited
        output:
            random road
        """
        shuffle(cities)
        return Road(cities)

    @staticmethod
    def calculateDistance(cities):
        """
        used for calculating the distance of a road
        input:
            cities - list of cities that need to be visited
        output:
            number representing the distance of the road
        """
        distanceSum = 0
        for i in range(len(cities) - 1):
            distanceSum += cities[i].distance(cities[i+1])
        return distanceSum

if __name__ == "__main__":
    pass
