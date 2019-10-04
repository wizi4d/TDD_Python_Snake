from graphics import *

import config
import game_view
from game_model import GameWorld, WorldStates

game = GameWorld()
window = GraphWin("Snake", config.SCENE_WIDTH * config.TILE_SIZE + 1, config.SCENE_HEIGHT * config.TILE_SIZE + 1, False)
renderer = game_view.Renderer(window, config.TILE_SIZE)


def start_game_loop():
    renderer.draw_scene(game)
    last_frame_time = time.time_ns()
    while game.state is WorldStates.Running:
        current_time = time.time_ns()
        dt = current_time - last_frame_time
        handle_input()
        if dt >= config.TICK_TIME:
            last_frame_time = current_time
            game.take_turn()
            renderer.draw_scene(game)
        time.sleep(0.05)


def handle_input():
    key = window.checkKey()
    if key == "Left" or key == "a":
        game.snake.turn_left()
    elif key == "Right" or key == "d":
        game.snake.turn_right()
    elif key == "q":
        game.state = WorldStates.Lost


start_game_loop()
window.close()
