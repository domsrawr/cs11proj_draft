# dito located mga data para madali iimport sa other py files
run_game = True
win = False
lose = False
mushroom_count = 0
max_mushroom_count = 0
tile_consequence = ''
item_holding = None

def reset():
    global run_game, win, lose, mushroom_count, tile_consequence, item_holding
    run_game = True
    win = False
    lose = False
    mushroom_count = 0
    tile_consequence = ''
    item_holding = None

def mushroom_counter(tiles):
    global max_mushroom_count
    for row_number in range(len(tiles)):
        if '+' in tiles[row_number]:
            for column_number in range(len(tiles[row_number])):
                if tiles[row_number][column_number] == '+':
                    max_mushroom_count += 1