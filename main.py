import os
import stagefile_reader
import movement
import display
import state
import copy
from argparse import ArgumentParser

# add more documentation! more structured documentation

def main():
    parser = ArgumentParser()
    parser.add_argument('stage_file')
    args = parser.parse_args()

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
                game_over_input(gamestate, tiles, original_tiles)
            elif gamestate['lost']:
                clear()
                display.convert_to_str(tiles)
                display.lose()
                game_over_input(gamestate, tiles, original_tiles)

def game_over_input(gamestate, tiles, original_tiles):
    input_sequence = input()
    for i in range(len(input_sequence)):
        if input_sequence[i] == '!':
            tiles[:] = copy.deepcopy(original_tiles)
            state.reset(gamestate, tiles)
            process_inputs(input_sequence[i:], gamestate, tiles, original_tiles)

def process_inputs(input_sequence, gamestate, tiles, original_tiles):
    for move in input_sequence:
        if move.upper() in 'WASD':
            movement.do_move(move.upper(), gamestate, tiles)
        elif move.upper() == 'P':
            movement.pick_up(gamestate)
        elif move == '!':
            tiles[:] = copy.deepcopy(original_tiles)
            state.reset(gamestate, tiles)
        else:
            break
        if not gamestate['run_game']:
            break

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
main()
