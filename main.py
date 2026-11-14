
#NOTE: THE BELOW CODE IS FOR THE 8-PUZZLE. REWORK IT LATER FOR THE 24-PUZZLE.

import sys
from puzzle import PuzzleState

def parse_input():
    """
    Accept arbitrary input from user.
    """
    print("--- 8-Puzzle Solver Program ---")
    print("Enter your unsolved puzzle as integers separated by spaces.")
    print("Use '0' to represent the blank space in the puzzle board.")
    print("Example for the 8-puzzle: 1 2 3 4 0 5 6 7 8")

    user_input = input("\nEnter initial state: ").strip()
    try:
        board = [int(x) for x in user_input.split()]
    except ValueError:
        print("Error: PLease enter valid integers only.")
        sys.exit(1)

    total_tiles = len(board)
    if total_tiles == 9:
        size = 3
    elif total_tiles == 25:
        size = 5
    else:
        print(f"Error: Invalid number of tiles ({total_tiles}). You can only have 9 tiles (for the 8-puzzle) or 25 tiles (for the 24-puzzle).")
        sys.exit(1)

    return board, size

def print_board(board, size):
    """
    Outputs the board grid layout into the terminal.
    """
    for i in range(0, len(board), size):
        row = board[i:i + size]
        print(" ".join(f"{val:2}" if val != 0 else " _" for val in row))
    print("-" * 15)

def main():
    board, size = parse_input()
    print("\nInitial Board Layout:")
    print_board(board, size)

    initial_state = PuzzleState(board, size=size)

    print(f"Heuristics for initial state:")
    print(f"  - h1(x), Misplaced Tiles: {initial_state.h1_misplaced()}")
    print(f"  - h2(x), Manhattan Distance: {initial_state.h2_manhatten()}")

    # A* SOLVER EXECUTION STUFF GOES HERE.

if __name__ == "__main__":
    main()