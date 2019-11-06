from chromosome import Chromosome
from operator import attrgetter
from point import Point
import random


class Fitting:
    POPULATION_SIZE = 30
    NUMBER_OF_GENERATIONS = 50

    def __init__(self, points, degree):
        self.points = points
        self.degree = int(degree)
        self.population = self.generateInitialPopulation()

    def generateInitialPopulation(self):
        population = list(map(lambda _: Chromosome(
            size=self.degree+1, points=self.points), range(self.POPULATION_SIZE)))
        self.bestEver = population[0]
        return population

    def fitness(self):
        return list(map(lambda i: i.fitness(), self.population))

    def selection(self):
        fitness = self.fitness()
        sumFitness = sum(fitness)
        rand = random.random() * sumFitness
        # print(sumFitness, rand)
        partialSum = sumFitness
        for i in range(self.POPULATION_SIZE):
            partialSum -= fitness[i]
            if partialSum <= rand:
                return self.population[i]

    def next(self):
        # print(self)
        parentOne = self.selection()
        parentTwo = self.selection()
        childOne, childTwo = parentOne.crossOver(parentTwo)
        childOne.mutate()
        childTwo.mutate()
        self.population += [childOne, childTwo]
        self.removeWeak()

    def removeWeak(self, number=2):
        for i in range(number):
            self.population.remove(
                max(self.population, key=lambda x: x.fitness()))

    def setBest(self):
        bestFit = self.bestEver.fitness()
        for i in self.population:
            if(bestFit > i.fitness()):
                self.bestEver = i
                bestFit = i.fitness()
        return self.bestEver

    def evolve(self):
        for i in range(self.NUMBER_OF_GENERATIONS):
            self.next()
            self.setBest()

    def __str__(self):
        return str(",".join(str(x.fitness()) for x in self.population))
