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
    
    larry_row, larry_column, mushroom_count, axe_tiles, flamethrower_tiles, paved_tiles = tile_finder(grid)

    gamestate = gamestate | {
        'larry_row': larry_row,
        'larry_column': larry_column,
        'max_mushroom_count': mushroom_count,
        'axe_tiles': axe_tiles,
        'flamethrower_tiles': flamethrower_tiles,
        'paved_tiles': paved_tiles,
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

def tile_finder(
        grid: list[list[str]],
) -> tuple:
    """Track all the important tiles in the grid.

    Searches the grid for specific tiles and returns their
    count or coordinate.

    Args:
        grid (list[list[str]]): The forest's 2D grid

    Returns:
        tup: A tuple of all the tiles' coordinates/counts. 
    """
    larry_row = 0
    larry_column = 0
    mushroom_count = 0
    axe_tiles = set()
    flamethrower_tiles = set()
    paved_tiles = set()

    for row_number in range(len(grid)):
        if any(item in '+Lx*_' for item in grid[row_number]):
            for column_number in range(len(grid[row_number])):
                if grid[row_number][column_number] == '+':
                    mushroom_count += 1
                elif grid[row_number][column_number] == 'L':
                    larry_row = row_number
                    larry_column = column_number
                elif grid[row_number][column_number] == 'x':
                    axe_tiles.add((row_number, column_number))
                elif grid[row_number][column_number] == '*':
                    flamethrower_tiles.add((row_number, column_number))
                elif grid[row_number][column_number] == '_':
                    paved_tiles.add((row_number, column_number))

    return larry_row, larry_column, mushroom_count, axe_tiles, flamethrower_tiles, paved_tiles
