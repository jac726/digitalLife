from individual import Individual
import random
from tkinter.constants import W


class Environment:

    def __init__(self, squareSize, foodOccurence, numIndividuals):
        self.environment = [
            [[] for x in range(squareSize)] for x in range(squareSize)]
        self.populateFood(squareSize, foodOccurence)
        self.generateIndividuals(numIndividuals, squareSize)
        return self

    def getPos(self, x, y):
        return self.environment[x][y]

    def hasIndividual(self, x, y):
        for x in self.environment[x][y]:
            if type(x) == Individual:
                return True

        return False

    def populateFood(self, squareSize, foodOccurence):
        for foodOccurence in range(foodOccurence):
            x_coord = random.randint(0, squareSize)
            y_coord = random.randint(0, squareSize)
            if len(self.environment[x_coord, y_coord]) != 0:
                self.environment[x_coord, y_coord].append(Food(squareSize/10))

    def generateIndividuals(self, numIndividuals, squareSize):
        def individualRowHelper(row, targetNum, squareSize):
            successful = 0
            while successful != targetNum:
                place = random.randint(0, squareSize)
                if not self.hasIndividual(row, place):
                    self.environment[row][place].append(Individual())
                    successful += 1

        def individualColHelper(col, targetNum, squareSize):
            successful = 0
            while successful != targetNum:
                place = random.randint(0, squareSize)
                if not self.hasIndividual(place, col):
                    self.environment[place][col].append(Individual())
                    successful += 1

        individualRowHelper(0, squareSize/4, squareSize)
        individualRowHelper(-1, squareSize/4, squareSize)
        individualColHelper(0, squareSize/4, squareSize)
        individualColHelper(-1, squareSize/4, squareSize)

        def step(self):
            # step forward a single instance of time
            # will have to invoke Individual class commands
            return None


class Food:

    def __init__(self, amountFood=10):
        self.foodQuantity = amountFood

    def eat(self):
        if self.foodQuantity - 10 < 0:
            return False
        else:
            self.foodQuanity -= 10
            return True

    def getFood(self):
        return self.foodQuantity
