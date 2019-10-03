import copy

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

    # region snake turns
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

    # endregion

    # region snake movement
    def test_should_move_snake_up(self):
        snake = self.game_world.snake
        assert snake.direction is Directions.Up
        prev_head_pos = copy.copy(snake.body[0])

        self.game_world.take_turn()

        cur_head_pos = snake.body[0]
        assert cur_head_pos.x == prev_head_pos.x
        assert cur_head_pos.y == prev_head_pos.y - 1

        cur_2nd_part_pos = snake.body[1]
        assert cur_2nd_part_pos == prev_head_pos

    def test_should_move_snake_right(self):
        snake = self.game_world.snake
        assert snake.direction is Directions.Up
        prev_head_pos = copy.copy(snake.body[0])

        self.game_world.snake.turn_right()
        self.game_world.take_turn()

        cur_head_pos = snake.body[0]
        assert cur_head_pos.x == prev_head_pos.x + 1
        assert cur_head_pos.y == prev_head_pos.y

        cur_2nd_part_pos = snake.body[1]
        assert cur_2nd_part_pos == prev_head_pos

    def test_should_move_snake_down(self):
        snake = self.game_world.snake
        assert snake.direction is Directions.Up
        prev_head_pos = copy.copy(snake.body[0])

        self.game_world.snake.turn_right()
        self.game_world.snake.turn_right()
        self.game_world.take_turn()

        cur_head_pos = snake.body[0]
        assert cur_head_pos.x == prev_head_pos.x
        assert cur_head_pos.y == prev_head_pos.y + 1

        cur_2nd_part_pos = snake.body[1]
        assert cur_2nd_part_pos == prev_head_pos

    def test_should_move_snake_left(self):
        snake = self.game_world.snake
        assert snake.direction is Directions.Up
        prev_head_pos = copy.copy(snake.body[0])

        self.game_world.snake.turn_left()
        self.game_world.take_turn()

        cur_head_pos = snake.body[0]
        assert cur_head_pos.x == prev_head_pos.x - 1
        assert cur_head_pos.y == prev_head_pos.y

        cur_2nd_part_pos = snake.body[1]
        assert cur_2nd_part_pos == prev_head_pos
    # endregion

    # region snake crawls over border
    def test_should_check_snake_crawl_over_top_border(self):
        snake = self.game_world.snake
        for _ in range(snake.body[0].y, 0, -1):
            self.game_world.take_turn()

        assert snake.body[0].y == config.SCENE_HEIGHT

    def test_should_check_snake_crawl_over_bottom_border(self):
        snake = self.game_world.snake
        snake.turn_left()
        snake.turn_left()
        for _ in range(snake.body[0].y, config.SCENE_HEIGHT + 1, 1):
            self.game_world.take_turn()

        assert snake.body[0].y == 1

    def test_should_check_snake_crawl_over_left_border(self):
        snake = self.game_world.snake
        snake.turn_left()
        for _ in range(snake.body[0].x, 0, -1):
            self.game_world.take_turn()

        assert snake.body[0].x == config.SCENE_WIDTH

    def test_should_check_snake_crawl_over_right_border(self):
        snake = self.game_world.snake
        snake.turn_right()
        for _ in range(snake.body[0].x, config.SCENE_WIDTH + 1, 1):
            self.game_world.take_turn()

        assert snake.body[0].x == 1
    # endregion
