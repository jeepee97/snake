from Food.Food import Food

class Banana(Food):
    def __init__(self, pos):
        super().__init__(pos)
        self.color = 0xFCEB11

    def getScore(self):
        return 1
