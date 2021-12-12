import random

mutateChance = 0.1
tournamentStrength = 5

class Evolvable:
    """
    interface class for the GA algorithm
    """
    def mutate(self, currentIter, allIter):
        """
        used for mutating the individual
        input:
            self
            currentIter - an individual should change its mutating intensity based upon how much 
                of the GA algorithm is left. currentIter and allIter is used to gage how much is left of
                the GA algorithm
            allIter - see currentIter
        output:
            NA
        """
        raise NotImplementedError(self.__class__ + ": mutate is not implemented")

    def crossbreed(self, partner):
        """
        used for crossbreading individuals
        input:
            self
            partner - the individual with which self will make offsprings
        output:
            two new individuals made from self and partner
        """
        raise NotImplementedError(self.__class__ + ": crossbreed is not implemented")

    def getFitness(self):
        """
        used for getting the viability of the individual. Bigger fitness means better individual.
        input:
            self
        output:
            real number, its meaning is the individuals' strength.
        """
        raise NotImplementedError(self.__class__ + ": getFitness is not implemented")
    
    def printInfo(self):
        """
        used to print status of genetic algorithm
        input:
            self
        output:
            NA
        """
        raise NotImplementedError(self.__class__ + ": printInfo is not implemented")


def chooseParents(individuals):
    """
    Returns two parents chosen at random. Individuals with greater fitness have higher chances of being 
    chosen
    input:
        individuals - list of possible candidates
    output:
        a tuple of two parents
    """

    tournamentParticipants = random.sample(individuals, len(individuals)//tournamentStrength)

    #get the two best individuals by sorting only 2
    for i in range(2):
        for j in range(i+1,len(tournamentParticipants)):
            if tournamentParticipants[j].getFitness() > tournamentParticipants[i].getFitness():
                tournamentParticipants[j], tournamentParticipants[i] = tournamentParticipants[i], tournamentParticipants[j]

    return (tournamentParticipants[0], tournamentParticipants[1])

def GA(parents, numOfIter):
    """
    Genetic algorithm
    input:
        parents - startrting population set, must be even number of parents
        numOfIter - number of iterations that will be executed
    output:
        best found individual
    """

    populationSize = len(parents)
    i = 0
    while i < numOfIter:
        children = []

        #make children
        for n in range(populationSize//2):
            father, mother = chooseParents(parents)
            child1, child2 = father.crossbreed(mother)
            if(random.random() < mutateChance):
                child1.mutate(i,numOfIter)
                child2.mutate(i,numOfIter)
            children.append(child1)
            children.append(child2)

        #move the best parent to children
        bestParent = max(parents, key=lambda x : x.getFitness())
        worstChildIdx = min(range(len(children)), key=lambda x : children[x].getFitness())
        children[worstChildIdx] = bestParent

        print(str(i) + " ", end="")
        bestParent.printInfo()

        #advance population
        parents = children
        i += 1

    return max(parents, key=lambda x : x.getFitness())

