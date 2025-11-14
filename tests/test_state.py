import pytest
import src.state as state

def test_tile_finder_basic():
    # L = Larry, + = mushroom, x = axe, * = flamethrower, _ = paved
    sample_map = [
        ['L', '+', 'x', '_', '*'],
        ['+', '_', '+', '+', '_'],
        ['x', '+', '*', '_', ' '],
    ]
    larry_row, larry_column, mushroom_count, axe_tiles, flamethrower_tiles, paved_tiles = state.tile_finder(sample_map)
    assert larry_row == 0
    assert larry_column == 0
    assert mushroom_count == 5
    assert axe_tiles == {(0,2), (2,0)}
    assert flamethrower_tiles == {(0,4), (2,2)}
    assert paved_tiles == {(0,3), (1,1), (1,4), (2,3)}

def test_initialize_gamestate(sample_gamestate):
    # map_of_gamestate = [
    #         ["T", ".", "L"],
    #         ["+", "R", "~"],
    #         ["_", "x", "*"],
    #     ]
    gamestate = sample_gamestate
    expected_keys = {
        'run_game', 'win', 'lost', 'mushroom_count','item_holding', 'tile_item', 'larry_row', 'larry_column', 'max_mushroom_count', 'axe_tiles', 'flamethrower_tiles', 'paved_tiles'
    }
    assert expected_keys == set(gamestate.keys())
    assert gamestate['run_game'] == True
    assert gamestate['win'] == False
    assert gamestate['lost'] == False
    assert gamestate['mushroom_count'] == 0
    assert gamestate['max_mushroom_count'] == 1
    assert gamestate['item_holding'] is None
    assert gamestate['tile_item'] is None
    assert gamestate['larry_row'] == 0
    assert gamestate['larry_column'] == 2
    assert gamestate['paved_tiles'] == {(2,0)}
    assert gamestate['axe_tiles'] == {(2,1)}
    assert gamestate['flamethrower_tiles'] == {(2,2)}

def test_tile_finder_grid_no_special_tiles():
    sample_map = [
        [' ', ' ', ' '],
        [' ', 'L', ' '],
        [' ', ' ', ' ']
    ]
    larry_row, larry_column, mushroom_count, axe_tiles, flamethrower_tiles, paved_tiles = state.tile_finder(sample_map)
    assert larry_row == 1
    assert larry_column == 1
    assert mushroom_count == 0
    assert not axe_tiles
    assert not flamethrower_tiles
    assert not paved_tiles

def test_reset_gamestate_same_as_initialize():
    sample_map = [
        ["T", ".", "."],
        ["+", "R", "~",],
        ["_", "x", "L",],
    ]
    sample_intialize = state.initialize_gamestate(sample_map)
    sample_reset = state.reset(sample_map)
    assert sample_intialize == sample_reset
