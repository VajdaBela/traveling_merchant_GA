# traveling_merchant_GA
Solution to the traveling merchant problem using the genetic algorithm (GA)

## The problem
The traveling merchant problem is a problem where the merchant has to visit all the cities and return to the starting city. The goal is to find the shortest road. This problem can't be solved through brute force because the number of possible roads is too big. Hence, the solution requires some way of finding a good enough solution instead of finding the best solution.

## The solution idea
In this project the genetic algorithm is used. The idea is that we have a population, which consists of possible solution to the problem. We make a selection from this population by taking the best among them. Combine them to get the new population, discard the old one and keep doing this until a desired solution is reached.

We ensure that we are getting close to a good solution by taking the best of the population. However, by taking only the best, the individuals from the next population start to resemble each other. That's a bad characteristic of a population because then only a small part of the possible solutions are being evaluated and there is a high chance that good solutions will not be considered.

Hence mutation is introduced. When the next population is being made every individual has a chance to mutate. This way the algorithm introduces variety into the population and increases the chances that a better road will be found.

## The code
data_tsp.txt contains the coordinates of fictional cities which should be visited by the merchant. To run the program:

    python main.py <file>

Where <file> should be in the same format as data_tsp.txt
