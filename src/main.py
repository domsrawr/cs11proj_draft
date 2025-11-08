import os
import stagefile_reader
import movement
import display
import state
import copy
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('stage_file')
    args = parser.parse_args()

    print(args)

    tiles = stagefile_reader.get_grid(args.stage_file)
    original_tiles = copy.deepcopy(tiles)
    gamestate = state.initialize_gamestate(tiles)

    while True:
        while gamestate['run_game']:
            clear()
            display.convert_to_str(tiles)
            display.display_mushroom_count(gamestate)
            display.display_item_holding(gamestate)
            display.display_movement_instructions()
            display.tile_item(gamestate)
            input_sequence = input() 
            process_inputs(input_sequence, gamestate, tiles, original_tiles)
        else:
            if gamestate['win']:
                clear()
                display.convert_to_str(tiles)
                display.win_mushroom_count(gamestate)
                display.win()
                input_sequence = input()
                game_over_input(input_sequence, gamestate, tiles, original_tiles)
            elif gamestate['lost']:
                clear()
                display.convert_to_str(tiles)
                display.lose()
                input_sequence = input()
                game_over_input(input_sequence, gamestate, tiles, original_tiles)

def game_over_input(input_sequence, gamestate, tiles, original_tiles):
    for i in range(len(input_sequence)):
        if input_sequence[i] == '!':
            reset_game(gamestate, tiles, original_tiles)
            process_inputs(input_sequence[i:], gamestate, tiles, original_tiles)

def process_inputs(input_sequence, gamestate, tiles, original_tiles):
    for i in range(len(input_sequence)):
        move = input_sequence[i]
        if not gamestate['run_game']:
            if move == '!':
                reset_game(gamestate, tiles, original_tiles)
                game_over_input(input_sequence[i:], gamestate, tiles, original_tiles)
                break
            continue
        if move.upper() in 'WASD':
            movement.do_move(move.upper(), gamestate, tiles)
        elif move.upper() == 'P':
            movement.pick_up(gamestate)
        elif move == '!':
            reset_game(gamestate, tiles, original_tiles)
        else:
            break
        
def reset_game(gamestate, tiles, original_tiles):
    tiles[:] = copy.deepcopy(original_tiles)
    state.reset(gamestate, tiles)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

main()
