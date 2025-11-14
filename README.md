# Shroom Raider

## Table of contents

- [About]
- User Guide
  - Prerequisites
  - Running the Game
  - The Basics
  - Controls
- References

## 📖 About
Shroom Raider is a simple terminal-based game, focusing on a character named Larry who is controlled by the user. The game takes place in a forest, which is a grid of tiles. Larry must obtain all the mushrooms in the forest.

## User Guide

## Prerequisites
To run the game successfully, the user must install the ``emoji`` module and ``pytest`` module for unit testing. This can be done by running ``pip install emoji`` and ``pip install pytest`` on the terminal.

## Running the game
The game is ran on the terminal and can be ran in multiple ways.

### Stage file
The stage file is the forest grid where the game will take place. The user may opt to provide their own stage file, otherwise, a default stage file will be used. Stage files are in the format:
```
R C
TTTTT
T...T
T...T
TTTTT
```
where R represents the number of rows, and C represents the number of columns. The next lines will be made up of the grid's tiles. The forest has rows and columns between 3 and 30 inclusIve. 

An example of a proper stage file would be:
```
6 7
TTTTTTT
T...x.T
T.L...T
T.R+..T
T...+.T
TTTTTTT
```

If the user chooses not to put his own stage file and instead chooses to play the default stage instead, these are the possible commands he may input.
```
python3 shroom_raider.py
python3 -m shroom_raider
```

If the player wants to put his own stage file, he must use the ``-f`` flag. After using either of the commands above, he must add ``-f <stage_file>`` where ``<stage_file>`` is the .txt stage file.

As such, possible commands would be
```
python3 shroom_raider.py -f <stage_file>
python3 -m shroom_raider -f <stage_file>
```


### Including moves and output file
After inputting his owm stage file, the user may opt to use the ``-m`` and ``-o`` flags. When using the ``-m`` flag, the user must input a string of characters denoting the moves he wants Larry to make. The ``-o`` flag denotes the file where the resulting grid will be outputted. The ``-m`` and ``-o`` flags must always be used in tandem.

Possible commands utilizing the ``-m`` and ``-o`` flag would be:
```
python3 shroom_raider.py -f <stage_file> -m <moves> -o <output_file>
python3 -m shroom_raider -f <stage_file> -m <moves> -o <output_file>
```
Where ``<moves>`` is the string of moves and ``<output_file>`` is the .txt output file.

The output file contains the following:
- First line: Whether the game was cleared or not
- Second line: The number of rows and columns on the grid
- Next lines: The forest's state after the moves were executed.

An output file looks like this:
```
NO CLEAR
7 7
TTTTTTT
T...x.T
T..L..T
T.R+..T
T...+.T
TTTTTTT
```
In summary, all of commands below are valid and will make the game run. 
- <stage_file> is a .txt file containing the forest grid.
- <moves> is a sequence of moves to be run.
- <output_file> is where the aftermath of the moves is outputted.
```
python3 shroom_raider.py
python3 -m shroom_raider  
python3 shroom_raider.py -f <stage_file>
python3 -m shroom_raider -f <stage_file>
python3 shroom_raider.py -f <stage_file> -m <moves> -o <output_file>
python3 -m shroom_raider -f <stage_file> -m <moves> -o <output_file>
```

## The Basics

There are 9 possible tiles in the forest, each with their own mechanics.

- Larry
  - ASCII: ``L``
  - Emoji: 🧑
  - The character the player is controlling.

- Empty tiles
  - ASCII: ``.``
  - Emoji:
  - Tiles where Larry can move freely. Rocks can also be pushed to this tile.
 
- Rocks
  - ASCII: ``R``
  - Emoji: 🪨
  - Larry can push this tile towards the direction he is moving at, provided that there are no obstacles in the way of the rock (other rocks, trees, mushrooms, items).
 
- Trees
  - ASCII: ``T``
  - Emoji: 🌲
  - Larry cannot move past these tiles. However, axes and flamethrowers can be used on trees. An axe removes a single tree, and flamethrower burns all connected trees.
 
- Mushrooms
  - ASCII: ``+``
  - Emoji: 🍄
  - Mushrooms can be collected. There are a set amount of mushrooms in a forest, and Larry must collect them all.
 
- Water
  - ASCII: ``~``
  - Emoji: 🟦
  - Water tiles are deadly. If larry moves to a water tile, he drowns and the player loses the game.
 
- Paved tiles
  - ASCII: ``_``
  - Emoji: ⬜
  - Paved tiles act just like empty tiles. Paved tiles can be created by pushing a rock to a water tile.
 
- Axe
  - ASCII: ``x``
  - Emoji: 🪓
  - Larry can pick up the axe and use it on a tree. The tree is chopped down and turned into an empty tile.
 
- Flamethrower
  - ASCII: ``*``
  - Emoji: 🔥
  - Larry can pick up the flamethrower. If he walks to a tile with a tree, all trees connected to that tree are burnt. When trees are burned, they become empty tiles.
 

## Controls
The user can input a string of moves of any length, where each character represents an individual move. 

- ### Movement
  To move, the user can use the WASD controls (case-insensitive).
    - W - Larry attempts to move forward
    - S - Larry attempts to move backward
    - A - Larry attempts to move to the left
    - D - Larry attempts to move to the right

   If Larry is currently holding an item, and he can use the item on the tile he's going to, the item will be used on that tile. 
 
- ### Picking up items
  To pick up items, the user input P or p. If there is an item on the tile he is standing at, and he is not currently holding an item, Larry will successfully pick up the item. The item will be removed from the tile he is standing on. If Larry tries to pick up an item and fails, a feedback message is printed, explaining why he wasn't able to pick up the tile.

  ### Resetting a level
  The user may choose to reset the level, where the forest and his inventory will be reset. The game will then restart on a fresh state. To reset the level, the player must input '!'.

## References
To make the game, the primary resource used was the [Project Core](https://drive.google.com/drive/folders/1Gmf2f71rK62S6Nwnfiy4eRuj5VCPuFl2).
