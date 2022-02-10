from Food.Food import Food

class Apple(Food):
    def __init__(self, pos):
        super().__init__(pos)
        self.color = 0xFC4E11

    def getScore(self):
        return 3