class PuzzleState:
    def __init__(self, board, size=3, parent=None, move=None, cost=0):
        """
        Initialize a game board as a tuple of integers to represent the board.
        The size of the board is 3 x 3 (for 8-puzzle).
        The size of the board WILL BE changed to 5 x 5 (for 24-puzzle) later.
        """
        self.board = tuple(board)
        self.size = size
        self.parent = parent
        self.move = move
        self.cost = cost
        self.blank_index = self.board.index(0)
        total_tiles = size * size
        self.goal_board = tuple(list(range(1, total_tiles)) + [0])

    def __eq__(self, other):
        return isinstance(other, PuzzleState) and self.board == other.board

    def __hash__(self):
        return hash(self.board)

    def is_goal(self):
        return self.board == self.goal_board

    def get_neighbors(self):
        neighbors = []
        r, c = divmod(self.blank_index, self.size)
        directions = [
            (-1, 0, "UP"),
            (1, 0, "DOWN"),
            (0, -1, "LEFT"),
            (0, 1, "RIGHT")
        ]

        for dr, dc, move_name in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.size and 0 <= nc < self.size:
                next_index = nr * self.size + nc
                new_board = list(self.board)
                new_board[self.blank_index], new_board[next_index] = new_board[next_index], new_board[self.blank_index]
                neighbors.append(
                    PuzzleState(
                        board=new_board,
                        size=self.size,
                        parent=self,
                        move=move_name,
                        cost=self.cost + 1
                    )
                )
        return neighbors

    def h1_misplaced(self):
        """
        h1(x) heuristic function. Represents the number of misplaced tiles (doesn't include the blank tile)
        """
        count = 0
        for i, val in enumerate(self.board):
            if val != 0 and val != self.goal_board[i]:
                count += 1
        return count

    def h2_manhattan(self):
        """
        h2(x) heuristic function. Represents the sum of distances of every tile to its goal position.
        """
        distance = 0
        for i, val in enumerate(self.board):
            if val == 0:
                continue
            goal_idx = self.goal_board.index(val)
            current_r, current_c = divmod(i, self.size)
            goal_r, goal_c = divmod(goal_idx, self.size)
            distance += abs(current_r - goal_r) + abs(current_c - goal_c)
        return distance