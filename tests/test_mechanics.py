import pytest
import src.mechanics as mechanics

# map_of_sample_init == sample_map = [
#         ["_", ".", "L"],
#         ["x", "R", "~"],
#         ["T", "+", "*"],
#     ]

def test_one_move(sample_init, sample_map):
    larry_row = 0
    larry_col = 2
    mechanics.do_move("A", sample_init, sample_map)

    # Larry is on (0, 1)
    assert sample_init["larry_row"] == larry_row
    assert sample_init["larry_column"] == larry_col - 1

def test_multiple_moves(sample_init, sample_map):
    larry_row = 0
    larry_col = 2
    mechanics.do_move("A", sample_init, sample_map)
    mechanics.do_move("A", sample_init, sample_map)
    mechanics.do_move("S", sample_init, sample_map)
    mechanics.do_move("D", sample_init, sample_map)
    mechanics.do_move("W", sample_init, sample_map)

    # Larry is on (0, 1)
    assert sample_init["larry_row"] == larry_row
    assert sample_init["larry_column"] == larry_col - 1

def test_move_to_tree(sample_init, sample_map):
    larry_row = 0
    larry_col = 2
    mechanics.do_move("A", sample_init, sample_map)
    mechanics.do_move("A", sample_init, sample_map)
    mechanics.do_move("S", sample_init, sample_map)
    mechanics.do_move("S", sample_init, sample_map)
    mechanics.do_move("S", sample_init, sample_map)
    mechanics.do_move("S", sample_init, sample_map)
    mechanics.do_move("S", sample_init, sample_map)
    mechanics.do_move("S", sample_init, sample_map)
    mechanics.do_move("S", sample_init, sample_map)

    # Larry does not move from (1, 0) because of tree
    assert sample_init["larry_row"] == larry_row + 1
    assert sample_init["larry_column"] == larry_col - 2

def test_collect_mushroom(sample_init, sample_map):
    mushroom_count = sample_init["mushroom_count"]
    mechanics.do_move("A", sample_init, sample_map)
    mechanics.do_move("A", sample_init, sample_map)
    mechanics.do_move("S", sample_init, sample_map)
    mechanics.do_move("D", sample_init, sample_map)
    mechanics.do_move("S", sample_init, sample_map)

    # Larry gets 1 mushroom (and wins)
    assert sample_init["mushroom_count"] == mushroom_count + 1

def test_move_rock_freely(rocky_init, rocky_map):
    # rocky_map = [
    #     [".", "L", ".", "."],
    #     [".", "R", "R", "."],
    #     [".", ".", ".", "+"],
    # ]
    (rock1, rock2) = ((1,1), (1,2))
    mechanics.do_move("S", rocky_init, rocky_map)
    # Rock 1 and 2 respectively
    assert rocky_map[2][1] == "R"
    assert rocky_map[1][2] == "R"

def test_move_rock_with_object_in_front(rocky_init, rocky_map):
    mechanics.do_move("A", rocky_init, rocky_map)
    mechanics.do_move("S", rocky_init, rocky_map)
    mechanics.do_move("D", rocky_init, rocky_map)
    mechanics.do_move("D", rocky_init, rocky_map)
    mechanics.do_move("D", rocky_init, rocky_map)
    # Rock 1 and 2 respectively (unchanged)
    assert rocky_map[1][1] == "R"
    assert rocky_map[1][2] == "R"

def test_step_into_water(sample_init, sample_map):
    # map_of_sample_init == sample_map = [
    #         ["_", ".", "L"],
    #         ["x", "R", "~"],
    #         ["T", "+", "*"],
    #     ]
    mechanics.do_move("S", sample_init, sample_map)
    assert sample_init['lost'] == True

def test_push_rock_to_water_create_paved(sample_init, sample_map):
    mechanics.do_move("A", sample_init, sample_map)
    mechanics.do_move("A", sample_init, sample_map)
    mechanics.do_move("S", sample_init, sample_map)
    mechanics.do_move("D", sample_init, sample_map)
    assert sample_map[1][2] == "_"

def test_walkable_paved_tile(sample_init, sample_map):
    mechanics.do_move("A", sample_init, sample_map)
    mechanics.do_move("A", sample_init, sample_map)
    mechanics.do_move("S", sample_init, sample_map)
    mechanics.do_move("D", sample_init, sample_map)
    mechanics.do_move("D", sample_init, sample_map)
    mechanics.do_move("A", sample_init, sample_map)
    assert sample_map[1][2] == "_"
    assert not sample_init['lost']

def test_pickup_axe(pickup_init, pickup_map):
    # pickup_map = [
    #     ["T", "T", "T", "T"],
    #     ["T", "x", "*", "T"],
    #     ["T", ".", "L", "+"],
    # ]
    mechanics.do_move("A", pickup_init, pickup_map)
    mechanics.do_move("W", pickup_init, pickup_map)
    mechanics.pick_up(pickup_init)
    assert pickup_init['item_holding'] == "axe"

def test_pickup_flamethrower(pickup_init, pickup_map):
    mechanics.do_move("W", pickup_init, pickup_map)
    mechanics.pick_up(pickup_init)
    assert pickup_init['item_holding'] == "flamethrower"

def test_pick_up_while_with_other_item(pickup_init, pickup_map):
    mechanics.do_move("W", pickup_init, pickup_map)
    mechanics.pick_up(pickup_init)
    assert pickup_init['item_holding'] == "flamethrower"
    mechanics.do_move("A", pickup_init, pickup_map)
    mechanics.pick_up(pickup_init)
    assert pickup_init["item_holding"] == "flamethrower"
    mechanics.do_move("D", pickup_init, pickup_map)
    assert pickup_map[1][1] == "x"

def test_chop_tree(pickup_init, pickup_map):
    # pickup_map = [
    #     ["T", "T", "T", "T"],
    #     ["T", "x", "*", "T"],
    #     ["T", ".", "L", "+"],
    # ]
    mechanics.do_move("A", pickup_init, pickup_map)
    mechanics.do_move("W", pickup_init, pickup_map)
    mechanics.pick_up(pickup_init)
    assert pickup_init['item_holding'] == "axe"
    mechanics.do_move("A", pickup_init, pickup_map)
    mechanics.do_move("D", pickup_init, pickup_map)
    assert pickup_init['item_holding'] is None
    assert pickup_map[1][0] == "."

def test_burn_trees(pickup_init, pickup_map):
    mechanics.do_move("W", pickup_init, pickup_map)
    mechanics.pick_up(pickup_init)
    assert pickup_init['item_holding'] == "flamethrower"
    mechanics.do_move("W", pickup_init, pickup_map)
    mechanics.do_move("S", pickup_init, pickup_map)
    assert pickup_init['item_holding'] is None
    assert pickup_map[0][0] == "."
    assert pickup_map[0][1] == "."
    assert pickup_map[0][2] == "."
    assert pickup_map[0][3] == "."
    assert pickup_map[1][3] == "."
    assert pickup_map[1][0] == "."
    assert pickup_map[2][0] == "."

def test_within_bounds_basic():
    grid = [['.', '.'], ['.', '.']]
    assert mechanics.within_bounds(0, 0, grid)
    assert mechanics.within_bounds(1, 1, grid)
    assert not mechanics.within_bounds(-1, 0, grid)
    assert not mechanics.within_bounds(0, 2, grid)
