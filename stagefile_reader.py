def get_grid(file):
    """combines all functions to simplify process
    """
    return extract_grid_from_file(read_file(file))

def extract_grid_from_file(unformatted_stagefile):
    """formats raw content taken from read_file()
    gets forest tiles and formats them
    """
    separated_by_line = (list(unformatted_stagefile.split('\n')))
    given_grid = separated_by_line[1:]
    grid = list(list(row) for row in given_grid)
    return grid

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")
