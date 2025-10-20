import state

# trip ko lang to kasi idk mas naiintindihan if 'tree' nakalagay and nde 'T'
possible_tiles = {
    'tree': 'T',
    'empty': '.',
    'larry': 'L',
    'mushroom': '+',
    'rock': 'R',
    'water': '~',
    'paved': '_'
}

def movement_rules(larry_next_row, larry_next_column, tiles, direction):
    '''indicates rules (e.g. can't move past trees, etc)
    '''
    if tiles[larry_next_row][larry_next_column] == possible_tiles['tree']:
        return False
    if tiles[larry_next_row][larry_next_column] == possible_tiles['mushroom']:
        state.mushroom_count += 1
        return True
    if tiles[larry_next_row][larry_next_column] == possible_tiles['rock']:
        if tiles[larry_next_row + direction[0]][larry_next_column + direction[1]] in (possible_tiles['rock'], possible_tiles['tree'], possible_tiles['mushroom']):
            return False
        elif tiles[larry_next_row + direction[0]][larry_next_column + direction[1]] == possible_tiles['water']:
            state.tile_consequence.append('rock_water')
            return True
        else:
            state.tile_consequence.append('rock_forward')
            return True
    if tiles[larry_next_row][larry_next_column] == possible_tiles['water']:
        state.alive = False
        return False
    if tiles[larry_next_row][larry_next_column] == possible_tiles['paved']:
        state.tile_consequence.append('paved_step')
        return True
    else:
        return True