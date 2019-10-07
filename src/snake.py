from graphics import *

import config
import game_view
from game_model import GameWorld, WorldStates

game = GameWorld()
window = GraphWin("Snake", config.SCENE_WIDTH * config.TILE_SIZE + 1, config.SCENE_HEIGHT * config.TILE_SIZE + 1, False)
renderer = game_view.Renderer(window, config.TILE_SIZE)
cheat_code = ""


def start_game_loop():
    renderer.draw_scene(game)
    last_frame_time = time.time_ns()
    while game.state is WorldStates.Running:
        current_time = time.time_ns()
        delta_time = current_time - last_frame_time
        handle_input()
        if delta_time >= config.TICK_TIME:
            last_frame_time = current_time
            game.take_turn()
            renderer.draw_scene(game)
        time.sleep(0.005)
        if game.state is WorldStates.Won:
            renderer.draw_congratulation()
            window.getKey()
        elif game.state is WorldStates.Lost:
            renderer.draw_lost_message()
            window.getKey()


def handle_input():
    key = window.checkKey()
    global cheat_code
    if key == "i":
        cheat_code = "i"
    elif key in ["d", "q"]:
        cheat_code += key
        if cheat_code == "iddqd":
            snake = game.snake
            for _ in range(config.SCENE_HEIGHT * config.SCENE_WIDTH - len(snake.body) - 1):
                snake.feed()
    elif key:
        cheat_code = ""

    if key == "Left" or key == "a":
        game.snake.turn_left()
    elif key == "Right" or key == "d":
        game.snake.turn_right()
    elif key == "q" and cheat_code == "":
        game.state = WorldStates.Lost


start_game_loop()
window.close()
