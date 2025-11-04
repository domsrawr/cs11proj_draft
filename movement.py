import rules
import state
import stagefile_reader
import copy

movement_dict = {
    'W': (-1, 0),
    'S': (1, 0),
    'A': (0, -1),
    'D': (0, 1),
    'w': (-1, 0),
    's': (1, 0),
    'a': (0, -1),
    'd': (0, 1),
}


def larry_finder(tiles):
    '''finds larry's coordinates by searching for 'L' in forest tiles
    '''
    global larry_row, larry_column
    for row_number in range(len(tiles)):
        if 'L' in tiles[row_number]:
            for column_number in range(len(tiles[row_number])):
                if tiles[row_number][column_number] == 'L':
                    larry_row = row_number
                    larry_column = column_number
                
def main_move(str_of_moves, tiles):
    '''combines all movement functions for simplification
    dito rin nauupdate yung tiles at nalalagay yung 'L'
    '''
    for individual_move in str_of_moves:
        trail(tiles)
        if not update_larry(individual_move, tiles):
            break
        tiles[larry_row][larry_column] = 'L'
        if state.tile_consequence:
            tile_consequence(tiles, individual_move)
        if rules.win_checker():
            break
        

def tile_consequence(tiles,move):
    # idea: dict with consequence as key and tile as val
    global larry_row, larry_column
    dx,dy = movement_dict[move]
    larry_next_row = larry_row + dx
    larry_next_column = larry_column + dy
    if state.tile_consequence == 'rock_forward':
        tiles[larry_next_row][larry_next_column] = 'R'
    if state.tile_consequence == 'rock_water':
        tiles[larry_next_row][larry_next_column] = '_'
        state.paved_tiles.append((larry_next_row, larry_next_column))
    if state.tile_consequence == 'water_fall':
        tiles[larry_row][larry_column] = '~'
    if state.tile_consequence == 'axe_tile':
        if (larry_row, larry_column) not in state.axe_tiles:
            state.axe_tiles.append((larry_row, larry_column))
    state.tile_consequence = ''

def trail(tiles):
    global larry_row, larry_column
    if (larry_row, larry_column) not in state.paved_tiles and (larry_row, larry_column) not in state.axe_tiles:
        tiles[larry_row][larry_column] = '.'
    elif (larry_row, larry_column) in state.axe_tiles:
        tiles[larry_row][larry_column] = 'x'
    else:
        tiles[larry_row][larry_column] = '_'
    
def update_larry(individual_move, tiles):
    '''updates larry's coordinates using larry_row and larry_column variables
    also returns boolean value
    if True; for loop continues
    if False (e.g. did not input WASD); terminates for loop, all succeeding moves are not registered
    ^^^ nakalagay kasi sa project core na ganun so ganun
    '''
    global larry_row, larry_column

    if individual_move in movement_dict:
        dx, dy = movement_dict[individual_move]
        if rules.movement_rules(larry_row + dx, larry_column + dy, tiles, movement_dict[individual_move]):
            larry_row += dx; larry_column += dy
            return True
        else:
            pass; return True
    elif individual_move == '!':
        tiles[:] = copy.deepcopy(stagefile_reader.grid_copy)
        larry_finder(tiles)
        state.reset()
        return True
    elif individual_move in 'Pp':
        rules.pick_up(larry_row, larry_column, tiles)
    else:
        tiles[larry_row][larry_column] = 'L'
        return False
    
def dead_or_win(str_of_moves, tiles):
    for i in range(len(str_of_moves)):
        if str_of_moves[i] == '!':
            main_move(str_of_moves[i:], tiles)
            break
        else:
            pass
