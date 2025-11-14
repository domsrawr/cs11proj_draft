"""Stage file reader module for reading and parsing stage file.

This module handles the convertion of stage files into usable and
mutable lists.
"""

def get_grid(
        file: str,
) -> list[list[str]]:
    """Load and parse a stage file into a 2D grid.
    
    This is the main entry point for loading stage files. 
    It combines file reading and grid extraction into a single function.
    
    Args:
        file (str): Name/path of the stage file
        
    Returns:
        list[list[str]]: 2D grid where each inner list represents a row of tiles
        
    Raises:
        FileNotFoundError: If the specified file doesn't exist
    """
    return extract_grid_from_file(read_file(file))

def extract_grid_from_file(
        unformatted_stagefile: str
) -> list[list[str]]:
    """Parse raw stage file content into a 2D character grid.
    
    The stage file format has dimensions on the first line, followed by
    the actual grid. This function:
    1. Splits the content by newlines
    2. Skips the first line (dimensions)
    3. Converts each remaining line into a list of characters

    Args:
        unformatted_stagefile (str): Raw content from the stage file
        
    Returns:
        list[list[str]]: 2D grid of characters
    """
    separated_by_line = (list(unformatted_stagefile.split('\n')))
    given_grid = separated_by_line[1:]
    grid = list(list(row) for row in given_grid)
    return grid

def read_file(
        filename: str
) -> str:
    """Read the contents of a file as a string.
    
    Opens and reads the entire file using UTF-8 encoding.
    
    Args:
        filename (str): Name/path of the file to read
        
    Returns:
        str: Complete file contents as a string
        
    Raises:
        FileNotFoundError: Raises error if the file does not exist.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")
