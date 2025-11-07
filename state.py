def initialize_gamestate(tiles):
    '''returns gamestate based on tiles argument
    '''
    gamestate = {
    'run_game': True,
    'win': False,
    'lost': False,

    'mushroom_count': 0,
    'max_mushroom_count': 0,

    'item_holding': None,
    'tile_item': None,

    'paved_tiles': set(),
    'axe_tiles': set(),
    'flamethrower_tiles': set(),

    'larry_row': 0,
    'larry_column': 0,
    }

    larry_finder(gamestate, tiles)
    mushroom_counter(gamestate, tiles)
    axe_finder(gamestate, tiles)
    flamethrower_finder(gamestate, tiles)

    return gamestate

def reset(gamestate, tiles):
    '''resets the gamestate
    '''
    new_state = initialize_gamestate(tiles)
    gamestate.clear()
    gamestate.update(new_state)

def larry_finder(gamestate, tiles):
    '''finds larry's coordinates by searching for 'L' in forest tiles
    '''
    for row_number in range(len(tiles)):
        if 'L' in tiles[row_number]:
            for column_number in range(len(tiles[row_number])):
                if tiles[row_number][column_number] == 'L':
                    gamestate['larry_row'] = row_number
                    gamestate['larry_column'] = column_number

def mushroom_counter(gamestate, tiles):
    '''searches for mushrooms in tiles and adds it all to gamestate
    '''
    for row_number in range(len(tiles)):
        if '+' in tiles[row_number]:
            for column_number in range(len(tiles[row_number])):
                if tiles[row_number][column_number] == '+':
                    gamestate['max_mushroom_count'] += 1

def axe_finder(gamestate, tiles):
    '''gets coordinates of all axes in tiles
    '''
    for row_number in range(len(tiles)):
        if 'x' in tiles[row_number]:
            for column_number in range(len(tiles[row_number])):
                if tiles[row_number][column_number] == 'x':
                    gamestate['axe_tiles'].add((row_number, column_number))

def flamethrower_finder(gamestate, tiles):
    '''gets coordinates of all flamethrowers in tiles
    '''
    for row_number in range(len(tiles)):
        if '*' in tiles[row_number]:
            for column_number in range(len(tiles[row_number])):
                if tiles[row_number][column_number] == '*':
                    gamestate['flamethrower_tiles'].add((row_number, column_number))
