from emoji import emojize

letter_correspondence = {
    'T': ":evergreen_tree:",
    '.': "　",
    'L': ":person:",
    '+': ":mushroom:",
    'R': ":rock:",
    '~': ":blue_square:",
    '_': ":white_large_square:",
    'x': ":axe:",
    '*': ":fire:",
}
ascii_to_emoji = {k: {"correspondence": v, "emoji": emojize(v)} for k, v in letter_correspondence.items()}

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
                map.append(ascii_to_emoji[char]["emoji"] + " ")
            else:
                map.append(ascii_to_emoji[char]["emoji"])
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
    if tile_item == 'axe':
        return f'Tile contains: {emojize(':axe:')}'
    elif tile_item == 'flamethrower':
        return f'Tile contains: {emojize(':fire:')}'
    else:
        return f'Tile contains:'


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
    if item == 'axe':
        return f'Item holding: {emojize(':axe:')}'
    elif item == 'flamethrower':
        return f'Item holding: {emojize(':fire:')}'
    else:
        return f'Item holding:'