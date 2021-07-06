import random


class Individual:

    def __init__(self, size, baseStomach, costToMove, probToGrow=random.randint(1, 10)/10, probToLove=random.randint(1, 10)/10, strength=random.randint(1, 10)):
        self.individual = size
        self.stomachContents = baseStomach
        self.costToMove = costToMove
        self.probToGrow = probToGrow
        self.probToMove = 1 - probToGrow
        self.probToLove = probToLove
        self.strength = strength

    def getCostToMove(self):
        return self.costToMove

    def getStomachContents(self):
        return self.stomachContents

    def getSize(self):
        return self.size

    def getProbToGrow(self):
        return self.probToGrow

    def getProbToLove(self):
        return self.probToLove

    def getStrength(self):
        return self.strength

    def mate(self, secondIndividual):
        parent1stomach = self.getStomachContents()
        parent2stomach = secondIndividual.getStomachContents()
        childStomach = parent1stomach + parent2stomach / 2

        parent1move = self.getCostToMove()
        parent2move = secondIndividual.getCostToMove()
        childMove = parent1move + parent2move / 2

        parent1ProbToGrow = self.getProbToGrow()
        parent2ProbToGrow = secondIndividual.getProbToGrow()
        childProbToGrow = parent1ProbToGrow + parent2ProbToGrow / 2

        parent1ProbToLove = self.getProbToLove()
        parent2ProbToLove = secondIndividual.getProbToLove()
        childProbToLove = parent1ProbToLove + parent2ProbToLove / 2

        parent1strength = self.getStrength()
        parent2strength = secondIndividual.getStrength()
        childStrength = parent1strength + parent2strength / 2
        return Individual(childStomach, childMove, childProbToGrow, childProbToLove, childStrength)

    def fight(self, secondIndividual):

        if self.strength > secondIndividual.strength:
            return self
        elif self.strength == secondIndividual.strength:
            return self if random.random() <= .5 else secondIndividual
        else:
            return secondIndividual
