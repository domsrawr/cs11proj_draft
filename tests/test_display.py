import pytest
import display.display as display

def test_convert_to_emoji_basic():
    # Expect the correct emoji output per letter_correspondence and ascii_to_emoji using real emojize
    # This will use the actual emoji package or fallback unicode for some environments.
    grid = [
        ['L', '+'],
        ['T', '.'],
    ]
    res = display.convert_to_emoji(grid)
    # Build the expected string from ascii_to_emoji values as in convert_to_emoji
    expected = (
        display.ascii_to_emoji['L']["emoji"] + display.ascii_to_emoji['+']["emoji"] + "\n" +
        display.ascii_to_emoji['T']["emoji"] + display.ascii_to_emoji['.']["emoji"] + "\n"
    )
    assert res == expected

def test_tile_item_none():
    gs = {'tile_item': None}
    assert display.tile_item(gs) == "Tile contains:"

def test_tile_item_axe():
    gs = {'tile_item': 'axe'}
    # Should include the axe emoji
    axe_emoji = display.ascii_to_emoji['x']["emoji"]
    assert display.tile_item(gs) == f"Tile contains: {axe_emoji}"

def test_tile_item_flamethrower():
    gs = {'tile_item': 'flamethrower'}
    flamethrower_emoji = display.ascii_to_emoji['*']["emoji"]
    assert display.tile_item(gs) == f"Tile contains: {flamethrower_emoji}"

def test_display_mushroom_count():
    gs = {'mushroom_count': 2, 'max_mushroom_count': 5}
    assert display.display_mushroom_count(gs) == "\n2/5 mushroom collected!"

def test_display_item_holding_none():
    gs = {'item_holding': None}
    assert display.display_item_holding(gs) == "Item holding:"

def test_display_item_holding_axe():
    gs = {'item_holding': 'axe'}
    axe_emoji = display.ascii_to_emoji['x']["emoji"]
    assert display.display_item_holding(gs) == f"Item holding: {axe_emoji}"

def test_display_item_holding_flamethrower():
    gs = {'item_holding': 'flamethrower'}
    flamethrower_emoji = display.ascii_to_emoji['*']["emoji"]
    assert display.display_item_holding(gs) == f"Item holding: {flamethrower_emoji}"