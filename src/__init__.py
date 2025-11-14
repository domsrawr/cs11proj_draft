"""Source package for Laro_Craft

This package contains the source code of the base game.

Run python shroom_raider.py intermediate_forest.txt in this folder to play the game

Modules:

    mechanics:
        State module for initializing and resetting the game state.

        This module handles initialization and management of the game state dictionary, which tracks Larry's position, mushroom counts, held items, and win/lose status.

        All functions in this module are only called when the game starts or when the game is reset.

        The gamestate dictionary is mutable and is passed to functions throughout the game to track changes.

    state:
        Mechanics module for handling all game mechanics.

        This module handles all player movement, tile interactions, and game mechanics including:
            - Moving Larry in four directions (WASD)
            - Interacting with different tile types (trees, rocks, water, mushrooms, items)
            - Item pickup and usage (axes, flamethrowers)

"""