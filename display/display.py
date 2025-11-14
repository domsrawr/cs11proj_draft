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


def convert_to_emoji(
        grid: list[list[str]]
) -> str:
    """Convert and print the forest grid as emojis to the console.
    
    Args:
        grid (list[list[str]]): 2D grid where each inner list is a row of tile characters
    """
    map = []
    for row in grid:
        for char in row:
            if char == 'R':
                map.append(emoji.emojize(ascii_to_emoji.get(char, char), language='alias') + ' ')
            else:
                map.append(emoji.emojize(ascii_to_emoji.get(char, char), language='alias'))
        map.append("\n")
    return "".join(map)


def tile_item(
        gamestate: dict
) -> str:
    """Display what item (if any) is available on Larry's current tile.
    
    Args:
        gamestate (dict): Current game state

    Returns:
        str: What item the tile contains, if any
    """
    tile_item = gamestate['tile_item']
    if tile_item:
        return f'The tile contains {"an" if tile_item[0].lower() in "aeiou" else "a"} {tile_item}!'
    else:
        return f'There is no item at the tile.'


def display_mushroom_count(
        gamestate: dict
) -> str:
    """Display how many out of the max number of mushrooms have been collected.
    
    Args:
        gamestate (dict): Current game state

    Returns:
        str: Amount of mushrooms the player has collected out of total mushrooms in grid.
    """
    curr_mushrooms = gamestate['mushroom_count']
    total_mushrooms = gamestate['max_mushroom_count']
    return f'\n{curr_mushrooms}/{total_mushrooms} mushroom collected!'

def display_item_holding(
        gamestate: dict
) -> str:
    """Display what item (if any) Larry is currently holding.
    
    Args:
        gamestate (dict): Current game state

    Returns:
        str: What item the player is currently holding, if any
    """
    item = gamestate['item_holding']
    if item:
        return f'You are holding {"an" if item[0].lower() in "aeiou" else "a"} {item}.'
    else:
        return f'You are not holding anything.'
