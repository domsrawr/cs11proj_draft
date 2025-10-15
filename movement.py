import rules


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
        remove_trail(tiles)
        if not update_larry(individual_move, tiles):
            break
        tiles[larry_row][larry_column] = 'L'

def remove_trail(tiles):
    '''when larry moves to a new tile, his previous tile becomes empty tile
    '''
    global larry_row, larry_column
    tiles[larry_row][larry_column] = '.'

def update_larry(individual_move, tiles):
    '''updates larry's coordinates using larry_row and larry_column variables
    also returns boolean value
    if True; for loop continues
    if False (e.g. did not input WASD); terminates for loop, all succeeding moves are not registered
    ^^^ nakalagay kasi sa project core na ganun so ganun
    '''
    global larry_row, larry_column
    if individual_move in 'Ww' and rules.movement_rules(larry_row-1,larry_column,tiles):
        larry_row -= 1
        return True
    if individual_move in 'Ss' and rules.movement_rules(larry_row+1,larry_column,tiles):
        larry_row += 1
        return True
    if individual_move in 'Aa' and rules.movement_rules(larry_row,larry_column-1,tiles):
        larry_column -= 1
        return True
    if individual_move in 'Dd' and rules.movement_rules(larry_row,larry_column+1,tiles):
        larry_column += 1
        return True
    elif individual_move in 'WASDwasd':
        pass
        return True
    else:
        tiles[larry_row][larry_column] = 'L'
        return False
    

