import random
from enum import Enum

import config


class GameWorld:
    def __init__(self):
        self.height = config.SCENE_HEIGHT
        self.width = config.SCENE_WIDTH
        self.snake = Snake()
        self.apple = self._get_random_empty_field()

    def take_turn(self):
        self.snake.move()

    def _get_random_empty_field(self):
        free_pos, pos_is_free = Point2D(0, 0), False
        while not pos_is_free:
            pos_is_free = True
            free_pos.x = random.randrange(1, config.SCENE_WIDTH)
            free_pos.y = random.randrange(1, config.SCENE_HEIGHT)
            for snake_part in self.snake.body:
                if free_pos == snake_part:
                    pos_is_free = False
                    break
        return free_pos


class Snake:
    def __init__(self):
        self.body = []
        head = Point2D(config.SCENE_WIDTH // 2, config.SCENE_HEIGHT // 2)
        self.body.append(head)
        self.body.append(Point2D(head.x, head.y + 1))
        self.direction = Directions.Up

    @property
    def head(self):
        return self.body[0]

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
            self.head.y = config.SCENE_HEIGHT if self.head.y == 1 else self.head.y - 1
        elif self.direction is Directions.Right:
            self.head.x = 1 if self.head.x == config.SCENE_WIDTH else self.head.x + 1
        elif self.direction is Directions.Down:
            self.head.y = 1 if self.head.y == config.SCENE_HEIGHT else self.head.y + 1
        elif self.direction is Directions.Left:
            self.head.x = config.SCENE_WIDTH if self.head.x == 1 else self.head.x - 1


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
