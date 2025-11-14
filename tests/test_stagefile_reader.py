import pytest
import setup.grid_reader.stagefile_reader as stagefile_reader

def test_extract_grid_from_file_basic():
    sample_content = "3 3\nSYS\nTEM\nERR"
    expected_grid = [
        ['S', 'Y', 'S'],
        ['T', 'E', 'M'],
        ['E', 'R', 'R']
    ]
    assert stagefile_reader.extract_grid_from_file(sample_content) == expected_grid

def test_extract_grid_from_file_with_whitespace_lines():
    sample_content = "4 4\nSOYL\n\nATIN\nABBY"
    expected_grid = [
        ['S', 'O', 'Y', 'L'],
        [],
        ['A', 'T', 'I', 'N'],
        ['A', 'B', 'B', 'Y'],
    ]
    assert stagefile_reader.extract_grid_from_file(sample_content) == expected_grid

def test_read_file_and_get_grid(tmp_path):
    # Create a temporary file with grid content
    content = "2 2\nXY\nZW"
    file_path = tmp_path / "stage.txt"
    file_path.write_text(content, encoding='utf-8')

    expected_grid = [
        ['X', 'Y'],
        ['Z', 'W']
    ]
    # Test that get_grid works with a temp file
    assert stagefile_reader.get_grid(str(file_path)) == expected_grid

def test_read_file_not_found():
    with pytest.raises(FileNotFoundError):
        stagefile_reader.read_file("schrodingersfile.txt")

def test_get_grid_file_not_found():
    with pytest.raises(FileNotFoundError):
        stagefile_reader.get_grid("ithinkthereforeiexist.txt")