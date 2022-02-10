from Food.Apple import Apple
from Food.Banana import Banana
from Food.Orange import Orange
import random

class FoodFactory():
    BANANA = 0
    ORANGE = 1
    APPLE = 2

    def createFood(snakeBody, foodOnMap, X, Y):
        food = []
        fruit = random.randint(0, 2)
        if (fruit == FoodFactory.BANANA):
            for i in range(3):
                if len(foodOnMap) + 1 > 10: break
                pos = FoodFactory.getValidPosition(snakeBody, foodOnMap, X, Y)
                food.append(Banana(pos))
        elif (fruit == FoodFactory.ORANGE):
            for i in range(2):
                if len(foodOnMap) + 1 > 10: break
                pos = FoodFactory.getValidPosition(snakeBody, foodOnMap, X, Y)
                food.append(Orange(pos))
        elif (fruit == FoodFactory.APPLE):
            for i in range(1):
                if len(foodOnMap) + 1 > 10: break
                pos = FoodFactory.getValidPosition(snakeBody, foodOnMap, X, Y)
                food.append(Apple(pos))
        else:
            print("erreur")

        return food

    def getValidPosition(snakeBody, foodOnMap, X, Y):
        x = 0
        y = 0
        while (True):
            x = random.randint(0, X)
            y = random.randint(0, Y)
            posInvalid = False
            for bodyPart in snakeBody:
                if (bodyPart == [x, y]):
                    posInvalid = True
            for f in foodOnMap:
                if (f.pos == [x,y]):
                    posInvalid = False
            if not posInvalid:
                break
        return [x,y]

