from individual import Individual
import random
from tkinter.constants import W


class Environment:

    def __init__(self, squareSize, foodOccurence, numIndividuals):
        self.environment = [
            [[] for x in range(squareSize)] for x in range(squareSize)]
        self.populateFood(squareSize, foodOccurence)
        self.generateIndividuals(numIndividuals, squareSize)
        self.foodCoordinates = []
        self.individualCoordinates = []
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
            self.environment[x_coord][y_coord].append(Food(squareSize/10))
            self.foodCoordinates.append((x_coord, y_coord))

    def generateIndividuals(self, numIndividuals, squareSize):
        def individualRowHelper(row, targetNum, squareSize):
            successful = 0
            while successful != targetNum:
                place = random.randint(0, squareSize)
                if not self.hasIndividual(row, place):
                    self.environment[row][place].append(Individual())
                    self.individualCoordinates.append((row, place))
                    successful += 1

        def individualColHelper(col, targetNum, squareSize):
            successful = 0
            while successful != targetNum:
                place = random.randint(0, squareSize)
                if not self.hasIndividual(place, col):
                    self.environment[place][col].append(Individual())
                    self.individualCoordinates.append((place, col))
                    successful += 1

        individualRowHelper(0, squareSize/4, squareSize)
        individualRowHelper(-1, squareSize/4, squareSize)
        individualColHelper(0, squareSize/4, squareSize)
        individualColHelper(-1, squareSize/4, squareSize)

    def distanceHelper(start, end):
        # Assuming there is no diagonal movement
        return abs(start[0]-end[0]) + abs(start[1]-end[1])

    def findNearestFood(self, start):
        retCoordinates = self.foodCoordinates[0]
        retMin = self.distanceHelper(start, self.foodCoordinates[0])

        pointer = 1
        while pointer < len(self.foodCoordinates):
            newCoordinates = self.foodCoordinates[pointer]
            if self.distanceHelper(start, newCoordinates) < retMin:
                retMin = self.distanceHelper(start, newCoordinates)
                retCoordinates = newCoordinates
            pointer += 1

        return retCoordinates

    def findNearestIndividual(self, start):
        retCoordinates = self.individualCoordinates[0]
        retMin = self.distanceHelper(start, self.individualCoordinates[0])

        pointer = 1
        while pointer < len(self.individualCoordinates):
            newCoordinates = self.individualCoordinates[pointer]
            if newCoordinates != start:
                if self.distanceHelper(start, newCoordinates) < retMin:
                    retMin = self.distanceHelper(start, newCoordinates)
                    retCoordinates = newCoordinates
                pointer += 1

        return retCoordinates

    def getClassAtPosList(self, currentPositionList, type):
        for thing in currentPositionList:
            if type(thing) == type:
                currentIndividual = thing
                break

    def removeClassAt(self, coordinates, type):
        currentList = self.getPos(coordinates)
        removed = False
        pointer = 0
        while not removed:
            if type(currentList[pointer]) == type:
                return currentList.pop(pointer)

    def step(self):
        for x_coord, y_coord in self.individualOccurences:
            currentPositionList = self.environment.getPos(x_coord, y_coord)
            currentIndividual = self.getClassAtPosList(
                currentPositionList, Individual)
            if not currentIndividual.getHasMoved():
                nearestFoodCoordinates = self.findNearestFood(
                    (x_coord, y_coord))
                nearestIndividualCoordinates = self.findNearestIndividual(
                    (x_coord, y_coord))
                nearestIndividual = self.getClassAtPosList(
                    self.getPos(nearestIndividualCoordinates), Individual)
                nearestFood = self.getClassAtPosList(
                    self.getPos(nearestFoodCoordinates), Food)
                if self.distanceHelper((x_coord, y_coord), nearestIndividualCoordinates) < 5:
                    if self.willFight(nearestIndividual):
                        if self.fight(nearestIndividual) == self:
                            self.removeClassAt(
                                nearestIndividualCoordinates, Individual)
                        else:
                            self.removeClassAt((x_coord, y_coord), Individual)
                elif self.willMate(nearestIndividual):
                    newIndividual = self.mate(nearestIndividual)
                    self.removeIndividualAt((x_coord, y_coord))
                    self.removeIndividualAt(nearestIndividualCoordinates)
                    self.getPos((x_coord, y_coord)).append(newIndividual)
                else:
                    distToFood = self.distanceHelper(
                        (x_coord, y_coord), nearestFoodCoordinates)
                    if distToFood < 2:
                        if nearestFood.eat():
                            currentIndividual.increaseStomachContents(10)
                        else:
                            self.deleteClassAt(nearestFoodCoordinates, Food)

                    distToFoodX = abs(x_coord - nearestFoodCoordinates[0])
                    distToFoodY = abs(y_coord - nearestFoodCoordinates[1])
                    movedIndividual = self.removeClassAt(
                        (x_coord, y_coord), Individual)

                    if distToFoodX > distToFoodY:
                        if nearestFoodCoordinates[1] > y_coord:
                            self.getPos((x_coord, y_coord+1)
                                        ).append(movedIndividual)
                        else:
                            self.getPos((x_coord, y_coord-1)
                                        ).append(movedIndividual)
                    else:
                        if nearestFoodCoordinates[0] > x_coord:
                            self.getPos((x_coord+1, y_coord)
                                        ).append(movedIndividual)
                        else:
                            self.getPos((x_coord-1, y_coord)
                                        ).append(movedIndividual)


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
