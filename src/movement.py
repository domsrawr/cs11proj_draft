movement_dict = {
    'W': (-1, 0),
    'S': (1, 0),
    'A': (0, -1),
    'D': (0, 1),
}

tile_symbols = {
    'tree': 'T',
    'empty': '.',
    'larry': 'L',
    'mushroom': '+',
    'rock': 'R',
    'water': '~',
    'paved': '_',
    'axe': 'x',
    'flamethrower': '*'
}
                
def do_move(direction, gamestate, tiles):
    row_offset, column_offset = movement_dict[direction]
    next_row = gamestate['larry_row'] + row_offset
    next_column = gamestate['larry_column'] + column_offset
    if within_bounds(next_row, next_column, tiles):
        can_move = tile_interactions(next_row, next_column, gamestate, tiles, row_offset, column_offset)
        if can_move:
            check_tile_item(next_row, next_column, gamestate, tiles)
            trail(gamestate['larry_row'], gamestate['larry_column'], gamestate, tiles)
            gamestate['larry_row'] = next_row
            gamestate['larry_column'] = next_column
            if should_overwrite_tile(gamestate):
                tiles[gamestate['larry_row']][gamestate['larry_column']] = tile_symbols['larry']
            

def should_overwrite_tile(gamestate):
    '''for readability purposes
    only time where larry doesn't overwrite the tile is when he drowns
    (the water consumes him)
    '''
    return not gamestate['lost']

def within_bounds(row, column, tiles):
    '''checks if row and column fall under forest tile dimensions
    '''
    return 0 <= row < len(tiles) and 0 <= column < len(tiles[0])        

def tile_interactions(next_row, next_column, gamestate, tiles, row_offset, column_offset):
    '''general function for tile interactions. passes to helper functions if complicated interaction
    returns boolean value. True if valid move or larry does move, False otherwise
    '''
    next_tile = tiles[next_row][next_column]
    if next_tile == tile_symbols['empty']:
        return True
    elif next_tile == tile_symbols['tree']:
        return tree_interactions(next_row, next_column, gamestate, tiles)
    elif next_tile == tile_symbols['rock']:
        return rock_interactions(next_row, next_column, gamestate, tiles, row_offset, column_offset)
    elif next_tile == tile_symbols['mushroom']:
        return mushroom_interactions(gamestate)
    elif next_tile == tile_symbols['paved']:
        return True
    elif next_tile == tile_symbols['water']:
        gamestate['run_game'] = False
        gamestate['lost'] = True
        return True
    elif next_tile == tile_symbols['axe']:
        return True
    elif next_tile == tile_symbols['flamethrower']:
        return True
    
def check_tile_item(next_row, next_column, gamestate, tiles):
    '''checks if there's an item in larry's next tile, None if no item
    only runs when can_move is True because tile_item can only changes if larry actually moves to next tile
    if can_move is False, larry still on same tile, so same tile_item, no need to check
    '''
    next_tile = tiles[next_row][next_column]
    item_map = {
        'x': 'axe',
        '*': 'flamethrower',
    }
    gamestate['tile_item'] = item_map.get(next_tile)

def tree_interactions(next_row, next_column, gamestate, tiles):
    '''if no item to cut/burn down tree, returns false
    '''
    if not gamestate['item_holding']:
        return False
    elif gamestate['item_holding'] == 'axe':
        gamestate['item_holding'] = None
        return True
    elif gamestate['item_holding'] == 'flamethrower':
        burn_connected_trees(next_row, next_column, tiles)
        gamestate['item_holding'] = None
        return True
    
def rock_interactions(rock_row, rock_column, gamestate, tiles, row_offset, column_offset):
    '''handles all cases for rock interactions and pushing.
    if rock's next position after being pushed is out of bounds, then invalid move
    '''
    rock_next_row = rock_row + row_offset
    rock_next_column = rock_column + column_offset

    if not within_bounds(rock_next_row, rock_next_column, tiles):
        return False
    
    rock_next_tile = tiles[rock_next_row][rock_next_column]
    
    if rock_next_tile in {
        tile_symbols['tree'],
        tile_symbols['rock'],
        tile_symbols['mushroom'],
        tile_symbols['axe'],
        tile_symbols['flamethrower']
    }:
        return False
    
    elif rock_next_tile == tile_symbols['water']:
        tiles[rock_next_row][rock_next_column] = tile_symbols['paved']
        gamestate['paved_tiles'].add((rock_next_row, rock_next_column))
        return True
    
    else:
        tiles[rock_next_row][rock_next_column] = tile_symbols['rock']
        return True
    
def mushroom_interactions(gamestate):
    '''adds 1 to mushroom collected. if all are collected, player wins
    always returns True as all moves to mushrooms are valid
    '''
    gamestate['mushroom_count'] += 1
    if gamestate['mushroom_count'] == gamestate['max_mushroom_count']:
        gamestate['run_game'] = False
        gamestate['win'] = True
    return True

def trail(larry_row, larry_column, gamestate, tiles):
    ''' item tiles and paved tiles first because they're fewer in number
    '''
    if (larry_row, larry_column) in gamestate['paved_tiles']:
        tiles[larry_row][larry_column] = '_'
    elif (larry_row, larry_column) in gamestate['axe_tiles']:
        tiles[larry_row][larry_column] = 'x'
    elif (larry_row, larry_column) in gamestate['flamethrower_tiles']:
        tiles[larry_row][larry_column] = '*'
    else:
        tiles[larry_row][larry_column] = '.'
    
def pick_up(gamestate):
    '''if there's an item in the tile, larry picks it up
    '''
    if gamestate['tile_item']:
        gamestate['item_holding'] = gamestate['tile_item']
        gamestate['tile_item'] = None
        gamestate[f"{gamestate['item_holding']}_tiles"].remove((gamestate['larry_row'], gamestate['larry_column']))

def burn_connected_trees(origin_row, origin_column, tiles):
    '''for flame thrower
    gets all connected trees then "burns" them down (replace with empty tile)
    '''
    r = len(tiles); c = len(tiles[0])
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    trees_affected = set()
    def helper(tree_row, tree_column):
        if (tree_row, tree_column) in trees_affected:
            return
        elif not (0 <= tree_row < r) or not (0 <= tree_column < c):
            return
        elif tiles[tree_row][tree_column] == tile_symbols['tree']:
            trees_affected.add((tree_row, tree_column))
            for (row_offset, column_offset) in directions:
                helper(tree_row + row_offset, tree_column + column_offset)
    helper(origin_row, origin_column)
    for (tree_row, tree_column) in trees_affected:
        tiles[tree_row][tree_column] = tile_symbols['empty']


