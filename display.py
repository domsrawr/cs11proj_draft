import state

def convert_to_str(tiles):
    '''converts forest tiles to string as tiles is initially formatted as list
    '''
    print('\n'.join(list(''.join(row) for row in tiles)))

def display_movement_instructions():
    print('''
[W] to move up
[A] to move left
[S] to move down
[D] to move right
          ''')
    
def display_mushroom_count():
    print(f'\n{state.mushroom_count} mushroom collected!')