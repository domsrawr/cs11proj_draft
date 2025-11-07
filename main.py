import os
import sys
import stagefile_reader
import movement
import display
import state
import rules

# sets stagefile as 'filename' variable
filename = sys.argv[1]
# get forest tiles from stagefile
tiles = stagefile_reader.get_grid(filename)

# calls larry.finder function so that meron na larry_row & larry_column sa movement.py (kasi global variable sha dun)
# larry_row and larry_column are not defined here sa main.py\
movement.larry_finder(tiles)
state.mushroom_counter(tiles)

while True:
    while state.run_game:
        os.system('cls' if os.name == 'nt' else 'clear')
        display.convert_to_str(tiles)
        display.display_mushroom_count()
        display.display_item_holding()
        display.display_movement_instructions()
        display.tile_item()
        str_of_moves = input() 
        movement.main_move(str_of_moves, tiles)
    else:
        if state.win:
            os.system('cls' if os.name == 'nt' else 'clear')
            display.convert_to_str(tiles)
            display.win_mushroom_count()
            display.win()
            str_of_moves = input() 
            movement.dead_or_win(str_of_moves, tiles)
        elif state.lose:
            os.system('cls' if os.name == 'nt' else 'clear')
            display.convert_to_str(tiles)
            display.lose()
            str_of_moves = input() 
            movement.dead_or_win(str_of_moves, tiles)