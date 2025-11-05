import state

def convert_to_str(tiles):
    """
    converts forest tiles to string as tiles is initially formatted as list
    """
    print('\n'.join(list(''.join(row) for row in tiles)))

def display_movement_instructions():
    print('''
    [W] to move up
    [A] to move left
    [S] to move down
    [D] to move right
    [P] to pick up an item
    [!] to reset the stage
    ''')

def tile_item():
    if state.tile_item:
        print(f'The tile contains an {state.tile_item}!')
    else:
        print(f'There is no item at the tile.')
    
def display_mushroom_count():
    print(f'\n{state.mushroom_count} mushroom collected!')

def display_item_holding():
    if state.item_holding:
        print(f'You are holding a {state.item_holding}')
    else:
        print(f'You are not holding anything.')

def win_mushroom_count():
    print(f"\nYou've collected {state.mushroom_count} mushrooms!")

def win():
    print('''
          _______                     _________ _        _ 
|\     /|(  ___  )|\     /|  |\     /|\__   __/( (    /|( )
( \   / )| (   ) || )   ( |  | )   ( |   ) (   |  \  ( || |
 \ (_) / | |   | || |   | |  | | _ | |   | |   |   \ | || |
  \   /  | |   | || |   | |  | |( )| |   | |   | (\ \) || |
   ) (   | |   | || |   | |  | || || |   | |   | | \   |(_)
   | |   | (___) || (___) |  | () () |___) (___| )  \  | _ 
   \_/   (_______)(_______)  (_______)\_______/|/    )_)(_)
    ''')
    
def lose():
    print('''
                
/\_/\___  _   _  | | ___  ___  ___       
\_ _/ _ \| | | | | |/ _ \/ __|/ _ \      
 / \ (_) | |_| | | | (_) \__ \  __/_ _ _ 
 \_/\___/ \__,_| |_|\___/|___/\___(_|_|_)
                                         
          ''')
    
