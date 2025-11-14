import pytest
import shroom_raider

# map_of_sample_init == sample_map = [
#         ["_", ".", "L"],
#         ["x", "R", "~"],
#         ["T", "+", "*"],
#     ]

def test_move_after_reset(sample_init, sample_map):
    orig_larry_row = 0
    orig_larry_col = 2
    orig_map = sample_map[:]
    shroom_raider.process_inputs("AASWS!A", sample_init, sample_map, orig_map)
    # Larry goes to from (0,2) -> (1,0) -> (0,2) [reset] -> (0,1)

    assert sample_init["larry row"] == orig_larry_row
    assert sample_init["larry column"] == orig_larry_col - 1

def test_move_after_invalid_character(sample_init, sample_map):
    orig_larry_row = 0
    orig_larry_col = 2
    orig_map = sample_map[:]
    shroom_raider.process_inputs("AA(+)POLLEN!EATERSDDAS", sample_init, sample_map, orig_map)
    # Larry goes to from (0,2) -> (0,0) -> (0,0) [invalid characters encountered]

    assert sample_init["larry row"] == orig_larry_row
    assert sample_init["larry column"] == orig_larry_col - 2