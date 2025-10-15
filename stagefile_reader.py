def get_grid(file):
    '''combines all functions to simplify process
    '''
    return extract_grid_from_file(read_file(file))

def extract_grid_from_file(unformatted_stagefile):
    '''formats raw content taken from read_file()
    gets number of rows, columns
    gets forest tiles and formats them
    '''
    separated_by_line = (list(unformatted_stagefile.split('\n')))
    rows, columns = separated_by_line[0].split(' ')
    given_grid = separated_by_line[1:]
    return list(list(row) for row in given_grid)

def read_file(filename):
    '''gets raw content of stagefile txt
    '''
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print('error, no file given')