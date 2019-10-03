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
        if self.direction == Directions.Up:
            self.direction = Directions.Left
        elif self.direction == Directions.Left:
            self.direction = Directions.Down
        elif self.direction == Directions.Down:
            self.direction = Directions.Right
        elif self.direction == Directions.Right:
            self.direction = Directions.Up


class Point2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Directions:
    Up = "up"
    Down = "down"
    Left = "left"
    Right = "right"
