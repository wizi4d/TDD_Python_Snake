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
        assert len(snake.body) == 2
        assert snake.direction is Directions.Up
        assert snake.head.x == config.SCENE_WIDTH // 2
        assert snake.head.y == config.SCENE_HEIGHT // 2

        apple = self.game_world.apple
        assert 0 < apple.x <= config.SCENE_WIDTH
        assert 0 < apple.y <= config.SCENE_HEIGHT

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
        prev_head_pos = copy.copy(snake.head)

        self.game_world.take_turn()

        assert snake.head.x == prev_head_pos.x
        assert snake.head.y == prev_head_pos.y - 1

        cur_2nd_part_pos = snake.body[1]
        assert cur_2nd_part_pos == prev_head_pos

    def test_should_move_snake_right(self):
        snake = self.game_world.snake
        assert snake.direction is Directions.Up
        prev_head_pos = copy.copy(snake.head)

        self.game_world.snake.turn_right()
        self.game_world.take_turn()

        assert snake.head.x == prev_head_pos.x + 1
        assert snake.head.y == prev_head_pos.y

        cur_2nd_part_pos = snake.body[1]
        assert cur_2nd_part_pos == prev_head_pos

    def test_should_move_snake_down(self):
        snake = self.game_world.snake
        assert snake.direction is Directions.Up
        prev_head_pos = copy.copy(snake.head)

        self.game_world.snake.turn_right()
        self.game_world.snake.turn_right()
        self.game_world.take_turn()

        assert snake.head.x == prev_head_pos.x
        assert snake.head.y == prev_head_pos.y + 1

        cur_2nd_part_pos = snake.body[1]
        assert cur_2nd_part_pos == prev_head_pos

    def test_should_move_snake_left(self):
        snake = self.game_world.snake
        assert snake.direction is Directions.Up
        prev_head_pos = copy.copy(snake.head)

        self.game_world.snake.turn_left()
        self.game_world.take_turn()

        assert snake.head.x == prev_head_pos.x - 1
        assert snake.head.y == prev_head_pos.y

        cur_2nd_part_pos = snake.body[1]
        assert cur_2nd_part_pos == prev_head_pos

    # endregion

    # region snake crawls over border
    def test_should_check_snake_crawl_over_top_border(self):
        snake = self.game_world.snake
        for _ in range(snake.head.y, 0, -1):
            self.game_world.take_turn()

        assert snake.head.y == config.SCENE_HEIGHT

    def test_should_check_snake_crawl_over_bottom_border(self):
        snake = self.game_world.snake
        snake.turn_left()
        snake.turn_left()
        for _ in range(snake.head.y, config.SCENE_HEIGHT + 1, 1):
            self.game_world.take_turn()

        assert snake.head.y == 1

    def test_should_check_snake_crawl_over_left_border(self):
        snake = self.game_world.snake
        snake.turn_left()
        for _ in range(snake.head.x, 0, -1):
            self.game_world.take_turn()

        assert snake.head.x == config.SCENE_WIDTH

    def test_should_check_snake_crawl_over_right_border(self):
        snake = self.game_world.snake
        snake.turn_right()
        for _ in range(snake.head.x, config.SCENE_WIDTH + 1, 1):
            self.game_world.take_turn()

        assert snake.head.x == 1

    # endregion

    # region food
    def test_should_place_apple_on_empty_random_field_on_init(self):
        new_world1 = GameWorld()
        for i in range(10):
            new_world2 = GameWorld()
            if new_world1.apple != new_world2.apple:
                break
        i += 1
        assert i < 10

    def test_should_feed_snake_with_apple(self):
        snake = self.game_world.snake
        self.game_world.apple.x = snake.head.x
        self.game_world.apple.y = snake.head.y - 1
        apple_pos_before_turn = copy.copy(self.game_world.apple)

        self.game_world.take_turn()

        assert snake.head == apple_pos_before_turn
        assert self.game_world.apple != apple_pos_before_turn
        assert len(snake.body) == 3
        assert snake.body[2] == snake.body[1]

    # endregion
