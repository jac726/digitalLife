import random


class Individual:

    def __init__(self, size, baseStomach, costToMove, probToGrow=random.randint(1, 10)/10):
        self.individual = size
        self.stomachContents = baseStomach
        self.costToMove = costToMove
        self.probToGrow = probToGrow
        self.probToMove = 1 - probToGrow

    def getCostToMove(self):
        return self.costToMove

    def getStomachContents(self):
        return self.stomachContents

    def getSize(self):
        return self.size

    def getProbToGrow(self):
        return self.probToGrow

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
        return Individual(childStomach, childMove, childProbToGrow)
