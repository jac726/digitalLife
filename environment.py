import random


class Environment:

    def __init__(self, squareSize, foodOccurence):
        self.basicEnvironment = [
            [[] for x in range(squareSize)] for x in range(squareSize)]

    def populateFood(self, squareSize, foodOccurence):
        for foodOccurence in range(foodOccurence):
            x_coord = random.randint(0, squareSize)
            y_coord = random.randint(0, squareSize)
            if len(self.environment[x_coord, y_coord]) != 0:
                self.environment[x_coord, y_coord].append(Food(squareSize/10))


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
