import os
import sys
import stagefile_reader
import movement
import display
import state


filename = sys.argv[1] #sets stagefile as 'filename' variable
tiles = stagefile_reader.get_grid(filename) #get forest tiles from stagefile
movement.larry_finder(tiles) 
# calls larry.finder function so that meron na larry_row & larry_column sa movement.py (kasi global variable sha dun)
# larry_row and larry_column are not defined here sa main.py
alive = True # kasi like pwede sha mamatay sa water dba

while alive:
    os.system('cls')
    display.convert_to_str(tiles)
    display.display_mushroom_count()
    display.display_movement_instructions()
    str_of_moves = input() 
    movement.main_move(str_of_moves, tiles)

