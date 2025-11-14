"""Main game module for handling flow of the game.

Handles:
- Command-line argument parsing
- Main game loop
- Input processing
- Game state management (running, win, lose)
- Stage resets
- Automated testing through output files
"""

import os
import copy
from setup import stagefile_reader
from src import state, mechanics, game_constants
from display import display
from argparse import ArgumentParser
def main() -> None:
    """Initialize and run shroom raider game.
    
    Parses command-line arguments to get the stage file, loads the forest grid,
    initializes game state, and enters the main game loop. If no stage file argument, 
    then a default stage file is used.

    If moves and output_file are present, run_automated_testing is executed which
    processes all moves then outputs the final state and grid to the output file.
    """

    parser = ArgumentParser()
    parser.add_argument('stage_file', nargs='?')
    parser.add_argument('-f', dest='file_arg')
    parser.add_argument('-m', dest='moves')
    parser.add_argument('-o', dest='output_file')
    args = parser.parse_args()

    stage_file = args.file_arg if args.file_arg else args.stage_file
    
    if not stage_file:
        stage_file = 'default_stage.txt'

    grid = stagefile_reader.get_grid(stage_file)
    original_grid = copy.deepcopy(grid)
    gamestate = state.initialize_gamestate(grid)

    if args.moves and args.output_file:
        run_automated_testing(args.moves, gamestate, grid, original_grid, args.output_file)
    else:
        run_live_gameplay(gamestate, grid, original_grid)


def run_automated_testing(
        moves: str,
        gamestate: dict,
        grid: list[list[str]],
        original_grid: list[list[str]],
        output_file: str,
) -> None:
    """Execute a sequence of moves then save results to file.
    
    This mode is used for automated testing. It processes all moves without
    user interaction and outputs the final state and grid to a file.
    
    Args:
        moves (str): String of moves to execute
        gamestate (dict): Current game state
        grid (list[list[str]]): Current forest grid
        original_grid (list[list[str]]): Original forest grid for reset
        output_file (str): Output file name
        
    Output file format:
        Line 1: "CLEAR" or "NO CLEAR"
        Line 2: Number of rows and columns
        Remaining lines: Final state of the forest grid
    """
    process_inputs(moves, gamestate, grid, original_grid)
    
    status = "CLEAR" if gamestate['win'] else "NO CLEAR"
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(f"{status}\n")
        file.write(f"{len(grid)} {len(grid[0])}\n")
        for row in grid:
            file.write(''.join(row) + '\n')

def run_live_gameplay(
        gamestate: dict,
        grid: list[list[str]],
        original_grid: list[list[str]],
) -> None:
    """Run the game in interactive mode with display and user input.
    
    Args:
        gamestate (dict): Current game state
        grid (list[list[str]]): Current forest grid
        original_grid (list[list[str]]): Original forest grid for reset
    """
    feedback_message = ''

    while True:
        while gamestate['run_game']:
            clear()
            print(display.convert_to_emoji(grid))
            print(display.display_mushroom_count(gamestate))
            print(display.display_item_holding(gamestate))
            print(display.tile_item(gamestate))
            if feedback_message:
                print('\n', feedback_message)
                feedback_message = ''
            print(game_constants.MOVEMENT_INSTRUCTIONS)
            input_sequence = input() 
            feedback_message = process_inputs(input_sequence, gamestate, grid, original_grid)
        else:
            if gamestate['win']:
                clear()
                print(display.convert_to_emoji(grid))
                print(display.display_mushroom_count(gamestate))
                print(game_constants.WIN_MESSAGE)
                input_sequence = input()
                game_over_input(input_sequence, gamestate, grid, original_grid)
            elif gamestate['lost']:
                clear()
                print(display.convert_to_emoji(grid))
                print(display.display_mushroom_count(gamestate))
                print(game_constants.LOSE_MESSAGE)
                input_sequence = input()
                game_over_input(input_sequence, gamestate, grid, original_grid)

def game_over_input(
        input_sequence: str,
        gamestate: dict,
        grid: list[list[str]],
        original_grid: list[list[str]],
) -> None:
    """Process input after the game is over (win or lose).
    
    When the game ends, this function waits for the player to press '!' to
    restart the level. Any other input is ignored. All moves after the '!'
    are processed.
    
    Args:
        input_sequence (str): String of input commands
        gamestate (dict): Current game state
        grid (list[list[str]]): Current forest grid
        original_grid (list[list[str]]): Original forest grid for reset
        
    Side Effects:
        Resets the game if '!' is found in the input sequence
    """
    for i in range(len(input_sequence)):
        if input_sequence[i] == '!':
            reset_game(gamestate, grid, original_grid)
            process_inputs(input_sequence[i:], gamestate, grid, original_grid)

def process_inputs(
        input_sequence: str,
        gamestate: dict,
        grid: list[list[str]],
        original_grid: list[list[str]],
) -> str:
    """Process a sequence of input commands.
    
    Handles multiple commands in a single input string:
    - W/A/S/D: Movement commands (case-insensitive)
    - P: Pick up item (case-insensitive)
    - !: Reset the stage
    - Other characters: Stops processing

    If the player dies or wins while the whole input sequence is still
    not processed, all subsequent moves are passed to game_over_input. 
    
    Args:
        input_sequence (str): String of input commands to process
        gamestate (dict): Current game state
        grid (list[list[str]]): Current forest grid
        original_grid (list[list[str]]): Original forest grid for reset

    Returns:
        str: If item pick up is not successful, returns reason why
        
    Side Effects:
        - Updates gamestate and tiles based on each command
        - Resets the game if '!' is encountered
        - Stops processing if invalid input
    """
    for i in range(len(input_sequence)):
        reason = ''
        picked_up = None
        move = input_sequence[i]
        if not gamestate['run_game']:
            game_over_input(input_sequence[i:], gamestate, grid, original_grid)
            break
        if move.upper() in 'WASD':
            mechanics.do_move(move.upper(), gamestate, grid)
        elif move.upper() == 'P':
            (picked_up, reason) = mechanics.pick_up(gamestate)
        elif move == '!':
            reset_game(gamestate, grid, original_grid)
        else:
            break
    if not picked_up:
        return reason
        
        
def reset_game(gamestate, grid, original_grid):
    """Reset the current stage to its initial state.
    
    Restores the forest grid to its original configuration and reinitializes
    the game state. Used when player presses '!' to restart.
    
    Args:
        gamestate (dict): Current game state to reset
        grid (list[list[str]]): Current forest grid to restore
        original_grid (list[list[str]]): Original forest grid to copy from
        
    Side Effects:
        - Restores grid to original configuration
        - Resets all gamestate values to initial state
    """
    grid[:] = copy.deepcopy(original_grid)
    new_state = state.reset(grid)
    gamestate.clear()
    gamestate.update(new_state)

def clear() -> None:
    """Clear the console screen.
    
    Uses the appropriate system command based on the operating system:
    - Windows: 'cls'
    - Unix/Linux/Mac: 'clear'
    """
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n")
        print("Exiting shroom raider... (Keyboard Interrupt detected)")
        print("\n")
