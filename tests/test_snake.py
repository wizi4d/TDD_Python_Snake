from src.model.GameModel import GameWorld, Directions


class TestSnake:
    def setup_method(self):
        self.game_world = GameWorld()

    def test_should_init_game_world(self):
        assert self.game_world.height == 10
        assert self.game_world.width == 10

        snake = self.game_world.snake
        assert snake is not None, "snake exists"
        assert len(snake.body) == 2
        assert snake.direction == Directions.Up
        assert snake.body[0].x == 5
        assert snake.body[0].y == 5

        apple = self.game_world.apple
        assert apple is not None, "apple exists"
        assert 0 <= apple.x < 10
        assert 0 <= apple.y < 10
