import state

# trip ko lang to kasi idk mas naiintindihan if 'tree' nakalagay and nde 'T'
possible_tiles = {
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

# maybe make new func for item consequences? or just do if not state.tile_consequence: ... else: ...

def pick_up(larry_row, larry_column, tiles):
    if tiles[larry_row][larry_column] == 'x':
        state.axe_tiles.remove((larry_row, larry_column))
        state.item_holding = 'axe'
    if tiles[larry_row][larry_column] == '*':
        state.flamethrower_tiles.remove((larry_row, larry_column))
        state.item_holding = 'flamethrower'

def flamethrower_affected(origin_row, origin_column, tiles):
    r = len(tiles); c = len(tiles[0])
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    affected = set()
    def helper(row, column):
        if (row, column) in affected:
            return
        elif not (0 <= row < r) or not (0 <= column < c):
            return
        elif tiles[row][column] == possible_tiles['tree']:
            affected.add((row, column))
            for (dx, dy) in dirs:
                helper(row + dx, column + dy)
    helper(origin_row, origin_column)
    return affected

def movement_rules(larry_next_row, larry_next_column, tiles, direction):
    '''indicates rules (e.g. can't move past trees, etc)
    '''
    if not (0 <= larry_next_row < len(tiles)) or not (0 <= larry_next_column < len(tiles[0])):
        return False

    state.tile_item = None

    tile = tiles[larry_next_row][larry_next_column]

    if tile == possible_tiles['water']:
        state.tile_consequence = 'water_fall'
        state.run_game = False
        state.lose = True
        return True

    elif tile == possible_tiles['tree']:
        if not state.item_holding:
            return False
        elif state.item_holding == 'axe':
            state.item_holding = None
            return True
        elif state.item_holding == 'flamethrower':
            state.item_holding = None
            affected_tiles = flamethrower_affected(larry_next_row, larry_next_column, tiles)
            for (row,column) in affected_tiles:
                tiles[row][column] = '.'
            return True
    
    elif tile == possible_tiles['rock']:
        next_row = larry_next_row + direction[0]
        next_column = larry_next_column + direction[1]
        next_tile = tiles[next_row][next_column]

        if next_tile in (
            possible_tiles['rock'], 
            possible_tiles['tree'], 
            possible_tiles['mushroom'],
            possible_tiles['axe']):
            return False
        
        elif not (0 <= next_row < len(tiles)) or not (0 <= next_column < len(tiles[0])):
            return False

        elif next_tile == possible_tiles['water']:
            state.tile_consequence = 'rock_water'
            return True
        
        else:
            state.tile_consequence = 'rock_forward'
            return True
        
    elif tile == possible_tiles['paved']:
        return True
    
    elif tile == possible_tiles['mushroom']:
        state.mushroom_count += 1
        if state.mushroom_count == state.max_mushroom_count:
            state.run_game = False
            state.win = True
        return True
    
    elif tile == possible_tiles['axe']:
        state.tile_consequence = 'axe_tile'
        state.tile_item = 'axe'
        return True
    
    elif tile == possible_tiles['flamethrower']:
        state.tile_consequence = 'flamethrower_tile'
        state.tile_item = 'flamethrower'
        return True
    
    else:
        return True
    

    
