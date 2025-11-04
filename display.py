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
[!] to reset the stage
          ''')
    
def display_mushroom_count():
    print(f'\n{state.mushroom_count} mushroom collected!')

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
                  _                               
/\_/\___  _   _  | | ___  ___  ___       
\_ _/ _ \| | | | | |/ _ \/ __|/ _ \      
 / \ (_) | |_| | | | (_) \__ \  __/_ _ _ 
 \_/\___/ \__,_| |_|\___/|___/\___(_|_|_)
                                         
          ''')