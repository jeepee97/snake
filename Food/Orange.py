from Food.Food import Food

class Orange(Food):
    def __init__(self, pos):
        super().__init__(pos)
        self.color = 0xfca311

    def getScore(self):
        return 2