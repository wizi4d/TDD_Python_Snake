from src.model.GameModel import GameWorld, Snake, Directions


class TestSnake:
    def test_should_init_game_world(self):
        game_world = GameWorld()
        assert game_world.height == 10
        assert game_world.width == 10

        assert game_world.snake != None, "snake exists"
        assert len(game_world.snake.body) == 2
        assert game_world.snake.direction == Directions.Up
        assert game_world.snake.body[0].x == 5
        assert game_world.snake.body[0].y == 5

        assert game_world.apple != None, "apple exists"
        assert game_world.apple.x >= 0 and game_world.apple.x < 10
        assert game_world.apple.y >= 0 and game_world.apple.y < 10
