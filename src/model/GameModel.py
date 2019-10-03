from enum import Enum

import config


class GameWorld:
    def __init__(self):
        self.height = config.SCENE_HEIGHT
        self.width = config.SCENE_WIDTH
        self.snake = Snake()
        self.apple = Point2D(1, 1)


class Snake:
    def __init__(self):
        self.body = [Point2D(5, 5), Point2D(5, 6)]
        self.direction = Directions.Up

    def turn_left(self):
        self.direction = self.direction.to_left()


class Point2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Directions(Enum):
    Up = 1
    Right = 2
    Down = 3
    Left = 4

    def to_left(self):
        return Directions(self.value - 1) if self is not Directions.Up else Directions.Left
