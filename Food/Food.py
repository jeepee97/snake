from abc import abstractmethod


class Food():
    def __init__(self, pos):
        self.pos = pos

    @abstractmethod
    def getScore(self):
        pass