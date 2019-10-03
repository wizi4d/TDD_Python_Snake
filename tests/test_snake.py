import config
from model.GameModel import GameWorld, Directions


class TestSnake:
    def setup_method(self):
        self.game_world = GameWorld()

    def test_should_init_game_world(self):
        assert self.game_world.height == config.SCENE_HEIGHT
        assert self.game_world.width == config.SCENE_WIDTH

        snake = self.game_world.snake
        assert snake is not None, "snake exists"
        assert len(snake.body) == 2
        assert snake.direction is Directions.Up
        assert snake.body[0].x == 5
        assert snake.body[0].y == 5

        apple = self.game_world.apple
        assert apple is not None, "apple exists"
        assert 0 <= apple.x < 10
        assert 0 <= apple.y < 10

    def test_should_turn_snake_left(self):
        snake = self.game_world.snake
        assert snake.direction is Directions.Up

        snake.turn_left()
        assert snake.direction is Directions.Left

        snake.turn_left()
        assert snake.direction is Directions.Down

        snake.turn_left()
        assert snake.direction is Directions.Right

        snake.turn_left()
        assert snake.direction is Directions.Up

    def test_should_turn_snake_right(self):
        snake = self.game_world.snake
        assert snake.direction is Directions.Up

        snake.turn_right()
        assert snake.direction is Directions.Right

        snake.turn_right()
        assert snake.direction is Directions.Down

        snake.turn_right()
        assert snake.direction is Directions.Left

        snake.turn_right()
        assert snake.direction is Directions.Up
