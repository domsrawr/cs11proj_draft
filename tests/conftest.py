import pytest
import src.state as state

@pytest.fixture
def sample_map():
    sample_map = [
        ["_", ".", "L"],
        ["x", "R", "~"],
        ["T", "+", "*"],
    ]
    return sample_map

@pytest.fixture
def rocky_map():
    rocky_map = [
        [".", "L", ".", "."],
        [".", "R", "R", "."],
        [".", ".", ".", "+"],
    ]
    return rocky_map

@pytest.fixture
def rocky_init(rocky_map):
    return state.initialize_gamestate(rocky_map)

@pytest.fixture
def sample_gamestate():
    sample_map = [
        ["T", ".", "L"],
        ["+", "R", "~"],
        ["_", "x", "*"],
    ]
    return state.initialize_gamestate(sample_map)

@pytest.fixture
def sample_init(sample_map):
    return state.initialize_gamestate(sample_map)

@pytest.fixture
def pickup_map():
    pickup_map = [
        ["T", "T", "T", "T"],
        ["T", "x", "*", "T"],
        ["T", ".", "L", "+"],
    ]
    return pickup_map

@pytest.fixture
def pickup_init(pickup_map):
    return state.initialize_gamestate(pickup_map)