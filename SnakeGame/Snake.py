from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Snake:
    #enlever les constantes et mettre des chiffres
    LEFT = 1
    RIGHT = 2
    DOWN = 3
    UP = 4

    def __init__(self):
        self.body = [[5, 10], [5, 11]]
        self.head = [self.body[0][0], self.body[0][1]]
        self.grow = False
        self.scoreToAdd = 0
        self.direction = Snake.RIGHT
        print("snake")

    def updateDirection(self, key):
        if key == Qt.Key_Left:
            if self.direction != Snake.RIGHT:
                self.direction = Snake.LEFT
        elif key == Qt.Key_Right:
            if self.direction != Snake.LEFT:
                self.direction = Snake.RIGHT
        elif key == Qt.Key_Down:
            if self.direction != Snake.UP:
                self.direction = Snake.DOWN
        elif key == Qt.Key_Up:
            if self.direction != Snake.DOWN:
                self.direction = Snake.UP
    
    def move(self, msg2statusbar):
        if self.direction == Snake.LEFT:
            self.head = [self.head[0] - 1, self.head[1]]
        if self.direction == Snake.RIGHT:
            self.head = [self.head[0] + 1, self.head[1]]
        if self.direction == Snake.DOWN:
            self.head = [self.head[0], self.head[1] + 1]
        if self.direction == Snake.UP:
            self.head = [self.head[0], self.head[1] - 1]

        self.body.insert(0, self.head)
        if (self.scoreToAdd == 0):
            self.body.pop()
        else:
            msg2statusbar.emit(str(len(self.body)-2))
            self.scoreToAdd -= 1