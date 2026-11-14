from puzzle import PuzzleState
from solver import a_star_search

def format_board_string(board, size):
    """
    Return a formatted string that represents the board.
    """
    lines = []
    for i in range(0, len(board), size):
        row = board[i:i + size]
        lines.append(" " + " ".join(f"{val:2}" if val != 0 else " _" for val in row))
    return "\n".join(lines)

def run_benchmark(file_handle, title, board, size, heuristics, max_ram_gb=4.0, max_frontier=3000000):
    """
    Run A* Search for the given board across the specified heuristics and logs to file.
    """
    file_handle.write("=" * 60 + "\n")
    file_handle.write(f"TEST CASE: {title}\n")
    file_handle.write("=" * 60 + "\n")
    file_handle.write("Initial Board:\n")
    file_handle.write(format_board_string(board, size) + "\n\n")

    initial_state = PuzzleState(board, size=size)

    for h in heuristics:
        h_label = "h1 (Misplaced Tiles)" if h == "h1" else "h2 (Manhattan Distance)"
        print(f"Running {title} with {h_label}...")
        file_handle.write(f"--- Heuristic: {h_label} ---\n")

        try:
            result = a_star_search(
                initial_state,
                heuristic_func_name = h,
                max_frontier_size = max_frontier,
                max_ram_gb = max_ram_gb
            )

            if result["success"]:
                file_handle.write(f"Status:             SUCCESS\n")
                file_handle.write(f"Time Elapsed:       {result['time_elapsed']:.6f} seconds\n")
                file_handle.write(f"Solution Length:    {result['cost']} moves\n")
                file_handle.write(f"States Explored:    {result['explored_nodes_count']}\n")
                file_handle.write(f"Peak Frontier:      {result['max_frontier']}\n")
                file_handle.write(f"Solution Path:      {' -> '.join(result['path'])}\n\n")
            else:
                file_handle.write("Status:              Failed/No solution found.\n\n")
        except MemoryError as e:
            print(f"RAM safeguard triggered for {title} ({h}): {e}")
            file_handle.write(f"Status:         Stopped/RAM Safeguard Triggered\n")
            file_handle.write(f"Details:        {e}\n\n")

def main():
    # 8-puzzle test cases (most likely will work even with RAM contraints)
    puzzle_8_easy = [1, 2, 3, 4, 0, 5, 6, 7, 8]
    puzzle_8_medium = [1, 3, 0, 4, 2, 5, 7, 8, 6]
    puzzle_8_hard = [8, 6, 7, 2, 5, 4, 3, 0, 1]

    # 24-puzzle test cases (most if not all prob won't work due to RAM contraints I put in this program due to my machine's limits. Sorry in advance :( )
    puzzle_24_medium = [
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 0, 14, 15,
        16, 17, 13, 18, 20,
        21, 22, 23, 19, 24
    ]

    puzzle_24_assignment_hard = [
        3, 17, 9, 5, 21,
        11, 0, 13, 19, 10,
        6, 24, 22, 1, 20,
        16, 14, 4, 12, 15,
        18, 8, 23, 2, 7
    ]

    with open("results.txt", "w", encoding="utf-8") as f:
        f.write("Informed Search (A* Search) Benchmark and Sample Solutions\n\n")

        run_benchmark(f, "8-Puzzle (Easy, 2 moves max)", puzzle_8_easy, 3, ["h1", "h2"])
        run_benchmark(f, "8-Puzzle (Medium)", puzzle_8_medium, 3, ["h1", "h2"])
        run_benchmark(f, "8-Puzzle (Hard, 31 moves max)", puzzle_8_hard, 3, ["h1", "h2"])

        run_benchmark(f, "24-Puzzle (Medium)", puzzle_24_medium, 5, ["h1", "h2"], max_ram_gb=4.0)
        run_benchmark(f, "24-Puzzle (Assignment, given)", puzzle_24_assignment_hard, 5, ["h2"], max_ram_gb=4.0)

    print("\nAll benchmarks complete. Results are written to `results.txt` file.")

if __name__ == "__main__":
    main()