"""Mechanics module for handling all game mechanics.

This module handles all player movement, tile interactions, and game mechanics including:
- Moving Larry in four directions (WASD)
- Interacting with different tile types (trees, rocks, water, mushrooms, items)
- Item pickup and usage (axes, flamethrowers)
"""


# Map movement keys to row and column offsets
movement_dict = {
    'W': (-1, 0),
    'S': (1, 0),
    'A': (0, -1),
    'D': (0, 1),
}

# Map tile names to their character symbols (for readability)
tile_symbols = {
    'tree': 'T',
    'empty': '.',
    'larry': 'L',
    'mushroom': '+',
    'rock': 'R',
    'water': '~',
    'paved': '_',
    'axe': 'x',
    'flamethrower': '*'
}
                
def do_move(
        direction: str,
        gamestate: dict,
        grid: list[list[str]],
) -> None:
    """Attempt to move Larry in the specified direction.
    
    Calculates the next position based on direction, checks if the position is within bounds, 
    determines if the move is valid based on tile interactions (trees, rocks, water, etc.), 
    and updates both the gamestate and tiles grid if Larry successfully moves.
    
    Args:
        direction (str): Movement direction ('W', 'A', 'S', or 'D')
        gamestate (dict): Current game state
        grid (list[list[str]]): 2D grid of forest tiles
        
    Side Effects:
        - Updates Larry's position (larry_row, larry_column) in gamestate
        - Updates tiles to show Larry's new position with 'L'
        - Leaves trail (empty tile, item tile, or paved tile) at old position
        - May collect mushrooms, use items, or trigger win/lose conditions
        - All updates only occur if the move is valid
    """
    row_offset, column_offset = movement_dict[direction]
    next_row = gamestate['larry_row'] + row_offset
    next_column = gamestate['larry_column'] + column_offset
    if within_bounds(next_row, next_column, grid):
        can_move = tile_interactions(next_row, next_column, gamestate, grid, row_offset, column_offset)
        if can_move:
            check_tile_item(next_row, next_column, gamestate, grid)
            trail(gamestate['larry_row'], gamestate['larry_column'], gamestate, grid)
            gamestate['larry_row'] = next_row
            gamestate['larry_column'] = next_column
            if should_overwrite_tile(gamestate):
                grid[gamestate['larry_row']][gamestate['larry_column']] = tile_symbols['larry']
            
def should_overwrite_tile(
        gamestate: dict
) -> bool:
    """Determine if Larry's new tile should be overwritten with 'L'.
    
    Larry doesn't overwrite the tile when he drowns in water,
    as the water consumes him visually.
    
    Args:
        gamestate (dict): Current game state
        
    Returns:
        bool: True if tile should be overwritten, False if Larry has lost (drowned)
    """
    return not gamestate['lost']

def within_bounds(
        row: int,
        column: int,
        tiles: list[list[str]],
) -> bool:
    """Check if the given position is within the forest tile boundaries.
    
    Args:
        row (int): Row index to check
        column (int): Column index to check
        tiles (list[list[str]]): 2D grid of forest tiles
        
    Returns:
        bool: True if position is within bounds, False otherwise
    """
    return 0 <= row < len(tiles) and 0 <= column < len(tiles[0])        

def tile_interactions(
        next_row: int,
        next_column: int,
        gamestate: dict,
        grid: list[list[str]],
        row_offset: int,
        column_offset: int,
) -> bool:
    """Handle interactions with the tile Larry is trying to move to.
    
    Different tiles have different behaviors:
    - Empty/Paved: Always passable
    - Tree: Requires axe or flamethrower
    - Rock: Can be pushed if there are no obstacles
    - Mushroom: Collected when walked over
    - Water: Causes instant loss
    - Items: Passable (can be picked up with 'P')
    
    Args:
        next_row (int): Row of the target tile
        next_column (int): Column of the target tile
        gamestate (dict): Current game state
        grid (list[list[str]]): 2D grid of forest tiles
        row_offset (int)
        : Vertical movement direction
        column_offset (int): Horizontal movement direction
        
    Returns:
        bool: True if Larry can move to the tile, False otherwise
        
    Side Effects:
        - May update gamestate (mushrooms, items held, win/lose status)
        - May modify tiles (burning trees, pushing rocks)
    """
    next_tile = grid[next_row][next_column]
    if next_tile == tile_symbols['empty']:
        return True
    elif next_tile == tile_symbols['tree']:
        return tree_interactions(next_row, next_column, gamestate, grid)
    elif next_tile == tile_symbols['rock']:
        return rock_interactions(next_row, next_column, gamestate, grid, row_offset, column_offset)
    elif next_tile == tile_symbols['mushroom']:
        return mushroom_interactions(gamestate)
    elif next_tile == tile_symbols['paved']:
        return True
    elif next_tile == tile_symbols['water']:
        gamestate['run_game'] = False
        gamestate['lost'] = True
        return True
    elif next_tile == tile_symbols['axe']:
        return True
    elif next_tile == tile_symbols['flamethrower']:
        return True
    
def check_tile_item(
        next_row: int,
        next_column: int,
        gamestate: dict,
        grid: list[list[str]],
) -> None:
    """Check if there's an item on the tile Larry's going to move to.
    
    Updates gamestate to indicate if an axe or flamethrower is available
    for pickup on Larry's next position.

    Only runs when can_move is True, as tile_item can only change when
    Larry actually moves to a different tile.
    
    Args:
        next_row (int): Row of the next tile
        next_column (int): Column of the next tile
        gamestate (dict): Current game state
        grid (list[list[str]]): 2D grid of forest tiles
        
    Side Effects:
        Updates gamestate['tile_item'] to 'axe', 'flamethrower', or None
    """
    next_tile = grid[next_row][next_column]
    item_map = {
        'x': 'axe',
        '*': 'flamethrower',
    }
    gamestate['tile_item'] = item_map.get(next_tile)

def tree_interactions(
        next_row: int,
        next_column: int,
        gamestate: dict,
        grid: list[list[str]],
) -> bool:
    """Handle interactions with tree tiles.
    
    Larry can only move through trees if he has an item that will allow
    him to destroy the tree. Otherwise, he cannot move to the next tile.

    Trees can be destroyed using either:
    - Axe: Removes single tree
    - Flamethrower: Burns all connected trees
    
    Args:
        next_row (int): Row of the tree
        next_column (int): Column of the tree
        gamestate (dict): Current game state
        grid (list[list[str]]): 2D grid of forest tiles
        
    Returns:
        bool: True if Larry has a tool to remove the tree, False otherwise
        
    Side Effects:
        - Consumes the held item (axe or flamethrower)
        - Burns connected trees if using flamethrower
    """
    if not gamestate['item_holding']:
        return False
    elif gamestate['item_holding'] == 'axe':
        gamestate['item_holding'] = None
        return True
    elif gamestate['item_holding'] == 'flamethrower':
        burn_connected_trees(next_row, next_column, grid)
        gamestate['item_holding'] = None
        return True
    
def rock_interactions(
        rock_row: int,
        rock_column: int,
        gamestate: dict,
        grid: list[list[str]],
        row_offset: int,
        column_offset: int,
) -> bool:
    """Handle pushing rocks and their interactions with other tiles.
    
    Rocks can be pushed only if the tile where it's going to be pushed is:
    - within bounds
    - an empty, paved, or water tile

    If the tile where the rock is going to be pushed is a water tile,
    a paved tile is made and it's added to the paved_tiles gamestate.
    
    Args:
        rock_row (int): Row of the rock
        rock_column (int): Column of the rock
        gamestate (dict): Current game state
        grid (list[list[str]]): 2D grid of forest tiles
        row_offset (int): Direction of push (vertical)
        column_offset (int): Direction of push (horizontal)
        
    Returns:
        bool: True if rock can be pushed, False otherwise
        
    Side Effects:
        - Moves rock to new position
        - Converts water to paved tile if rock is pushed into water
        - Updates gamestate['paved_tiles'] when creating paved tiles
    """
    rock_next_row = rock_row + row_offset
    rock_next_column = rock_column + column_offset

    if not within_bounds(rock_next_row, rock_next_column, grid):
        return False
    
    rock_next_tile = grid[rock_next_row][rock_next_column]
    
    if rock_next_tile in {
        tile_symbols['tree'],
        tile_symbols['rock'],
        tile_symbols['mushroom'],
        tile_symbols['axe'],
        tile_symbols['flamethrower']
    }:
        return False
    
    elif rock_next_tile == tile_symbols['water']:
        grid[rock_next_row][rock_next_column] = tile_symbols['paved']
        gamestate['paved_tiles'].add((rock_next_row, rock_next_column))
        return True
    
    else:
        grid[rock_next_row][rock_next_column] = tile_symbols['rock']
        return True
    
def mushroom_interactions(
        gamestate: dict
) -> bool:
    """Handle collecting a mushroom.
    
    Increments the mushroom count and checks for win condition.
    If all mushrooms are collected, the game is won.
    
    Args:
        gamestate (dict): Current game state
        
    Returns:
        bool: Always True (moving to mushroom is always valid)
        
    Side Effects:
        - Increments mushroom_count
        - Sets win=True and run_game=False if all mushrooms collected
    """
    gamestate['mushroom_count'] += 1
    if gamestate['mushroom_count'] == gamestate['max_mushroom_count']:
        gamestate['run_game'] = False
        gamestate['win'] = True
    return True

def trail(
        old_row: int,
        old_column: int,
        gamestate: dict,
        grid: list[list[str]] ,
) -> None:
    """Update the tile Larry is leaving behind as he moves.
    
    Restores the original tile type after Larry moves away:
    - Paved tiles stay paved
    - Item tiles show the item again (if not picked up)
    - Other tiles become empty

    Checks item tiles and paved tiles first as they're fewer in number,
    improving performance.

    Args:
        old_row (int): Row Larry is leaving
        old_column (int): Column Larry is leaving
        gamestate (dict): Current game state
        grid (list[list[str]]): 2D grid of forest tiles
        
    Side Effects:
        Updates grid at (old_row, old_column) to show appropriate symbol
    """
    if (old_row, old_column) in gamestate['paved_tiles']:
        grid[old_row][old_column] = '_'
    elif (old_row, old_column) in gamestate['axe_tiles']:
        grid[old_row][old_column] = 'x'
    elif (old_row, old_column) in gamestate['flamethrower_tiles']:
        grid[old_row][old_column] = '*'
    else:
        grid[old_row][old_column] = '.'
    
def pick_up(
        gamestate: dict
) -> None:
    """Pick up an item from Larry's current tile.
    
    If there's an item on the current tile, Larry picks it up and the item
    is removed from the tile and from the item coordinate tracking set.
    Larry must not be holding an item for him to pick up at the item at the
    current tile.

    If Larry tries to pick up an item when there's no item on the tile,
    nothing happens.
    
    Args:
        gamestate (dict): Current game state
        
    Side Effects:
        - Sets item_holding to the picked up item
        - Clears tile_item
        - Removes the item coordinates from the set that tracks it
    """
    if gamestate['tile_item'] and not gamestate['item_holding']:
        gamestate['item_holding'] = gamestate['tile_item']
        gamestate['tile_item'] = None
        gamestate[f"{gamestate['item_holding']}_tiles"].remove((gamestate['larry_row'], gamestate['larry_column']))

def burn_connected_trees(
        origin_row: int,
        origin_column: int,
        grid: list[list[str]],
) -> None:
    """Burn down all trees connected to the origin tree using flamethrower.
    
    Uses depth-first search (DFS) to find all trees that are connected 
    (up, down, left, right) to the targeted tree, then removes them.
    
    Args:
        origin_row (int): Row of the tree being targeted
        origin_column (int): Column of the tree being targeted
        grid (list[list[str]]): 2D grid of forest tiles
        
    Side Effects:
        Converts all connected tree tiles to empty tiles
    """
    r = len(grid); c = len(grid[0])
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    trees_affected = set()
    def helper(tree_row, tree_column):
        if (tree_row, tree_column) in trees_affected:
            return
        elif not (0 <= tree_row < r) or not (0 <= tree_column < c):
            return
        elif grid[tree_row][tree_column] == tile_symbols['tree']:
            trees_affected.add((tree_row, tree_column))
            for (row_offset, column_offset) in directions:
                helper(tree_row + row_offset, tree_column + column_offset)
    helper(origin_row, origin_column)
    for (tree_row, tree_column) in trees_affected:
        grid[tree_row][tree_column] = tile_symbols['empty']


