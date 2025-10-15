import state

# trip ko lang to kasi idk mas naiintindihan if 'tree' nakalagay and nde 'T'
possible_tiles = {
    'tree': 'T',
    'empty': '.',
    'larry': 'L',
    'mushroom': '+'
}

def movement_rules(larry_next_row, larry_next_column, tiles):
    '''indicates rules (e.g. can't move past trees, etc)
    '''
    if tiles[larry_next_row][larry_next_column] == possible_tiles['tree']:
        return False
    if tiles[larry_next_row][larry_next_column] == possible_tiles['mushroom']:
        state.mushroom_count += 1
        return True
    else:
        return True