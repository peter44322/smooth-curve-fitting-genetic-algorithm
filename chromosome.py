from equation import Equation
import random


class Chromosome:
    UPPER_BOUND = 10
    LOWER_BOUND = -10

    def __init__(self, size=0, coefficients=0, points=[]):
        if coefficients == 0:
            self.coefficients = self.generateRandom(size)
            self.size = size
        else:
            self.coefficients = coefficients
            self.size = len(coefficients)

        self.equation = Equation(self.coefficients)
        self.points = points

    def fitness(self):
        n = len(self.points)
        sum = 0
        for point in self.points:
            yCalc = self.equation.substituteX(point.x)
            sum += (yCalc - point.y) ** 2
        return round(sum/n, 6)

    def generateRandom(self, size):
        coefficients = []
        for i in range(size):
            coefficients.append(round(random.uniform(
                self.LOWER_BOUND, self.UPPER_BOUND), 6))
        return coefficients

    def crossOver(self, parent):
        intHalfLength = int(random.random() * self.size)+1
        childOne = Chromosome(coefficients=parent.coefficients[0:intHalfLength] +
                              self.coefficients[intHalfLength-1:])
        childTwo = Chromosome(coefficients=self.coefficients[0:intHalfLength] +
                              parent.coefficients[intHalfLength-1:])
        childOne.points = self.points
        childTwo.points = self.points
        return childOne, childTwo

    def mutate(self, rate=0.5):
        if(random.random() < rate):
            randomIndex = int(random.randrange(self.size))
            gene = self.coefficients[randomIndex]
            rand = random.random()
            deltaLower = gene - self.LOWER_BOUND
            deltaUpper = self.UPPER_BOUND - gene
            delta = deltaLower if rand <= 0.5 else deltaUpper
            rand = random.random() * delta
            newGene = gene - rand if delta == deltaLower else gene + rand
            self.coefficients[randomIndex] = round(newGene, 6)

    def __str__(self):
        return ",".join(str(x) for x in self.coefficients)

    def __eq__(self, other):
        return self.fitness() == other.fitness()
