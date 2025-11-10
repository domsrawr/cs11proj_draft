"""Display module for handling all console outputs.

This module is in charge of:
- Rendering the forest grid
- Displaying game instructions
- Showing player status (items, mushrooms)
- Win/lose screens
"""
import emoji

ascii_to_emoji = {
    'T': ":evergreen_tree:",
    '.': "　",
    'L': ":person:",
    '+': ":mushroom:",
    'R': ":rock:",
    '~': ":blue_square:",
    '_': ":white_large_square:",
    'x': ":axe:",
    '*': ":fire:"
}

def convert_to_emoji(grid):
    """Convert and print the forest grid as emojis to the console.
    
    Args:
        grid (list[list[str]]): 2D grid where each inner list is a row of tile characters
    """
    for row in grid:
        map = ''.join(
            (emoji.emojize(ascii_to_emoji.get(char, char), language='alias') + ' ') if char == 'R'
            else emoji.emojize(ascii_to_emoji.get(char, char), language='alias') for char in row)
        print(map)

def display_movement_instructions():
    """Displays movement and action controls"""
    print('''
    [W] to move up
    [A] to move left
    [S] to move down
    [D] to move right
    [P] to pick up an item
    [!] to reset the stage
          
What's your move?
    ''')

def tile_item(gamestate):
    """Display what item (if any) is available on Larry's current tile.
    
    Args:
        gamestate (dict): Current game state
    """
    tile_item = gamestate['tile_item']
    if tile_item:
        print(f'The tile contains {"an" if tile_item[0].lower() in "aeiou" else "a"} {tile_item}!')
    else:
        print(f'There is no item at the tile.')
    
def display_mushroom_count(gamestate):
    """Display how many out of the max number of mushrooms have been collected.
    
    Args:
        gamestate (dict): Current game state
    """
    print(f'\n{gamestate['mushroom_count']}/{gamestate['max_mushroom_count']} mushroom collected!')

def display_item_holding(gamestate):
    """Display what item (if any) Larry is currently holding.
    
    Args:
        gamestate (dict): Current game state
    """
    item = gamestate['item_holding']
    if item:
        print(f'You are holding {"an" if item[0].lower() in "aeiou" else "a"} {item}.')
    else:
        print(f'You are not holding anything.')

def win():
    """Display victory screen."""
    print('''
You won!
Input '!' to play again!
    ''')
    
def lose():
    """Display game over screen."""
    print('''
You lost...
Input '!' to play again!
    ''')
