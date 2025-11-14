def initialize_gamestate(
        grid: list[list[str]]
) -> dict:
    """Initialize and return a gamestate dictionary based on the forest's tiles.

    Args:
        grid (list[list[str]]): The forest's 2D grid where each string is a tile.

    Returns:
        dict: Game state containing:
            - run_game (bool): Whether the game loop should continue (not dead or hasn't won)
            - win (bool): Whether the player has won
            - lost (bool): Whether the player has lost
            - mushroom_count (int): Number of mushrooms collected
            - max_mushroom_count (int): Total mushrooms in the level
            - item_holding (str|None): Item Larry is currently holding ('axe', 'flamethrower', or None)
            - tile_item (str|None): Item available on Larry's current tile
            - paved_tiles (set): Coordinates of paved tiles
            - axe_tiles (set): Coordinates of all axe locations
            - flamethrower_tiles (set): Coordinates of all flamethrower locations
            - larry_row (int): Larry's current row position
            - larry_column (int): Larry's current column position
    """
    gamestate = {'run_game': True,
                 'win': False,
                 'lost': False,
                 'mushroom_count': 0,
                 'item_holding': None,
                 'tile_item': None,
                 }

    gamestate = gamestate | {
        'larry_row': (larry_finder(grid))[0],
        'larry_column': (larry_finder(grid))[1],
        'max_mushroom_count': mushroom_counter(grid),
        'axe_tiles': axe_finder(grid),
        'flamethrower_tiles': flamethrower_finder(grid),
        'paved_tiles': paved_finder(grid),
    }

    return gamestate

def reset(
        grid: list[list[str]],
) -> dict:
    """Reset the gamestate dictionary to its original values.

    Clears all gamestate data and reinitializes it using original game grid.
    Used when user inputs '!' to reset the level.

    Args: 
        grid (list[list[str]]): Original grid (before any moves were made)

    Returns:
        dict: Contains all the resetted game state values.
    """
    new_state = initialize_gamestate(grid)

    return new_state

def larry_finder(
        grid: list[list[str]],
) -> tuple:
    """Find Larry's initial position.

    Searches the grid for the 'L' character and returns
    Larry's row and column.

    Args:
        grid (list[list[str]]): The forest's 2D grid

    Returns:
        tuple: A tuple containing Larry's row and column.
    """
    for row_number in range(len(grid)):
        if 'L' in grid[row_number]:
            for column_number in range(len(grid[row_number])):
                if grid[row_number][column_number] == 'L':
                    return (row_number, column_number)

def mushroom_counter(
        grid: list[list[str]],
) -> int:
    """Count the total amount of mushrooms in the forest.

    Searches the grid for the '+' character and returns
    the total amount of mushrooms.

    Args:
        grid (list[list[str]]): The forest's 2D grid

    Returns:
        int: Total number of mushrooms in the grid
    """
    mushroom_count = 0
    for row_number in range(len(grid)):
        if '+' in grid[row_number]:
            for column_number in range(len(grid[row_number])):
                if grid[row_number][column_number] == '+':
                    mushroom_count += 1
    return mushroom_count

def axe_finder(
        grid: list[list[str]],
) -> set:
    """Find and store the coordinates of all tiles with an axe.

    Searches the grid for the 'x' character and returns all coordinates
    with the character.

    Args:
        grid (list[list[str]]): The forest's 2D grid

    Returns:
        set: All tiles with an axe.
    """
    axe_tiles = set()
    for row_number in range(len(grid)):
        if 'x' in grid[row_number]:
            for column_number in range(len(grid[row_number])):
                if grid[row_number][column_number] == 'x':
                    axe_tiles.add((row_number, column_number))
    return axe_tiles

def flamethrower_finder(
        tiles: list[list[str]],
) -> set:
    """Find and store the coordinates of all tiles with a flamethrower.

    Searches the grid for the '*' character and returns all coordinates
    with the character.

    Args:
        grid (list[list[str]]): The forest's 2D grid

    Returns:
        set: All tiles with a flamethrower.
    """
    flamethrower_tiles = set()
    for row_number in range(len(tiles)):
        if '*' in tiles[row_number]:
            for column_number in range(len(tiles[row_number])):
                if tiles[row_number][column_number] == '*':
                    flamethrower_tiles.add((row_number, column_number))
    return flamethrower_tiles

def flamethrower_finder(
        tiles: list[list[str]],
) -> set:
    """Find and store the coordinates of all tiles with a flamethrower.

    Searches the grid for the '*' character and returns all coordinates
    with the character.

    Args:
        grid (list[list[str]]): The forest's 2D grid

    Returns:
        set: All tiles with a flamethrower.
    """
    paved_tiles = set()
    for row_number in range(len(tiles)):
        if '_' in tiles[row_number]:
            for column_number in range(len(tiles[row_number])):
                if tiles[row_number][column_number] == '_':
                    paved_tiles.add((row_number, column_number))
    return paved_tiles