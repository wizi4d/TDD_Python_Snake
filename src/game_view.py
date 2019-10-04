from graphics import *

import config
from game_model import GameWorld, Point2D


class Renderer:
    def __init__(self, window: GraphWin, tile_size):
        self._window = window
        self._tile_size = tile_size

    def draw_scene(self, game: GameWorld):
        self.clear()
        self._draw_field()
        self._draw_apple(game)
        self._draw_snake(game)
        self._window.update()

    def clear(self):
        for item in self._window.items[:]:
            item.undraw()
        # self._window.update()

    def _draw_field(self):
        for x in range(config.SCENE_WIDTH):
            for y in range(config.SCENE_HEIGHT):
                self._draw_tile(x, y)

    def _draw_tile(self, x, y):
        corner1 = Point(x * self._tile_size, y * self._tile_size)
        corner2 = corner1.clone()
        corner2.move(self._tile_size, self._tile_size)
        tile = Rectangle(corner1, corner2)
        tile.draw(self._window)

    def _draw_apple(self, game: GameWorld):
        self._draw_game_object(game.apple, "red")

    def _draw_game_object(self, game_coord: Point2D, color: str):
        game_object = Circle(self._game_coord_to_screen(game_coord), (self._tile_size - 2) // 2)
        game_object.setFill(color)
        game_object.draw(self._window)

    def _game_coord_to_screen(self, point: Point2D):
        screen_x = (point.x - 1) * self._tile_size + self._tile_size // 2
        screen_y = (point.y - 1) * self._tile_size + self._tile_size // 2
        return Point(screen_x, screen_y)

    def _draw_snake(self, game: GameWorld):
        snake = game.snake
        self._draw_game_object(snake.head, "blue")
        for part in snake.body[1:]:
            self._draw_game_object(part, "green")
