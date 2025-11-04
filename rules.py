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
    'axe': 'x'
}

# maybe make new func for item consequences? or just do if not state.tile_consequence: ... else: ...

def win_checker():
    state.mushroom_count == state.max_mushroom_count
    state.run_game = False
    state.win = True


def pick_up(larry_row, larry_column, tiles):
    if tiles[larry_row][larry_column] == 'x':
        state.axe_tiles.remove((larry_row, larry_column))
        state.item_holding = 'axe'
        return True

def movement_rules(larry_next_row, larry_next_column, tiles, direction):
    '''indicates rules (e.g. can't move past trees, etc)
    '''
    if (0 > larry_next_row > len(tiles)-1) or (0 > larry_next_column > len(tiles[0])-1):
        return False

    tile = tiles[larry_next_row][larry_next_column]

    if tile == possible_tiles['water']:
        state.tile_consequence = 'water_fall'
        state.run_game = False
        state.lose = True
        return True

    elif tile == possible_tiles['tree']:
        if state.item_holding == 'axe':
            state.item_holding = None
            return True
        return False
    
    elif tile == possible_tiles['mushroom']:
        state.mushroom_count += 1
        return True
    
    elif tile == possible_tiles['axe']:
        state.tile_consequence = 'axe_tile'
        return True
    
    elif tile == possible_tiles['paved']:
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
        
        elif next_tile == possible_tiles['water']:
            state.tile_consequence = 'rock_water'
            return True
        
        else:
            state.tile_consequence = 'rock_forward'
            return True
        
    else:
        return True
    
