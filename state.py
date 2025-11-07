# dito located mga data para madali iimport sa other py files
run_game = True
win = False
lose = False
mushroom_count = 0
max_mushroom_count = 0
tile_consequence = ''
item_holding = None
tile_item = None
<<<<<<< HEAD
paved_tiles = set()
axe_tiles = set()
flamethrower_tiles = set()

def reset():
    global run_game, win, lose, mushroom_count, tile_item, item_holding, paved_tiles, axe_tiles, flamethrower_tiles
=======
paved_tiles = []
axe_tiles = []
flamethrower_tiles = []

def reset():
    global run_game, win, lose, mushroom_count, tile_consequence, tile_item, item_holding, paved_tiles, axe_tiles, flamethrower_tiles
>>>>>>> d1962a83548b60b00adf3926d4eeb75cf294c908
    run_game = True
    win = False
    lose = False
    mushroom_count = 0
    tile_item = None
    item_holding = None
<<<<<<< HEAD
    paved_tiles = set()
    axe_tiles = set()
    flamethrower_tiles = set()
=======
    paved_tiles = []
    axe_tiles = []
    flamethrower_tiles = []
>>>>>>> d1962a83548b60b00adf3926d4eeb75cf294c908


#smth about this
def mushroom_counter(tiles):
    global max_mushroom_count
    for row_number in range(len(tiles)):
        if '+' in tiles[row_number]:
            for column_number in range(len(tiles[row_number])):
                if tiles[row_number][column_number] == '+':
                    max_mushroom_count += 1