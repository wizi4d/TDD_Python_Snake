from enum import Enum

import config


class GameWorld:
    def __init__(self):
        self.height = config.SCENE_HEIGHT
        self.width = config.SCENE_WIDTH
        self.snake = Snake()
        self.apple = Point2D(1, 1)

    def take_turn(self):
        self.snake.move()


class Snake:
    def __init__(self):
        self.body = []
        head = Point2D(config.SCENE_WIDTH // 2, config.SCENE_HEIGHT // 2)
        self.body.append(head)
        self.body.append(Point2D(head.x, head.y + 1))
        self.direction = Directions.Up

    def turn_left(self):
        self.direction = self.direction.to_left()

    def turn_right(self):
        self.direction = self.direction.to_right()

    def move(self):
        self._move_body_without_head()
        self._move_head()

    def _move_body_without_head(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

    def _move_head(self):
        if self.direction is Directions.Up:
            self.body[0].y = config.SCENE_HEIGHT if self.body[0].y == 1 else self.body[0].y - 1
        elif self.direction is Directions.Right:
            self.body[0].x = 1 if self.body[0].x == config.SCENE_WIDTH else self.body[0].x + 1
        elif self.direction is Directions.Down:
            self.body[0].y = 1 if self.body[0].y == config.SCENE_HEIGHT else self.body[0].y + 1
        elif self.direction is Directions.Left:
            self.body[0].x = config.SCENE_WIDTH if self.body[0].x == 1 else self.body[0].x - 1


class Point2D:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point2D):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return self.__dict__.__repr__()


class Directions(Enum):
    Up = 1
    Right = 2
    Down = 3
    Left = 4

    def to_left(self):
        return Directions(self.value - 1) if self is not Directions.Up else Directions.Left

    def to_right(self):
        return Directions(self.value + 1) if self is not Directions.Left else Directions.Up
