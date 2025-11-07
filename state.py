# dito located mga data para madali iimport sa other py files
run_game = True
win = False
lose = False
mushroom_count = 0
max_mushroom_count = 0
tile_consequence = ''
item_holding = None
tile_item = None
paved_tiles = set()
axe_tiles = set()
flamethrower_tiles = set()

def reset():
    global run_game, win, lose, mushroom_count, tile_item, item_holding, paved_tiles, axe_tiles, flamethrower_tiles
    run_game = True
    win = False
    lose = False
    mushroom_count = 0
    tile_item = None
    item_holding = None
    paved_tiles = set()
    axe_tiles = set()
    flamethrower_tiles = set()


#smth about this
def mushroom_counter(tiles):
    global max_mushroom_count
    for row_number in range(len(tiles)):
        if '+' in tiles[row_number]:
            for column_number in range(len(tiles[row_number])):
                if tiles[row_number][column_number] == '+':
                    max_mushroom_count += 1