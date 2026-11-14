
#NOTE: THE BELOW CODE IS FOR THE 8-PUZZLE. REWORK IT LATER FOR THE 24-PUZZLE.

import heapq
import time
import os
import psutil
from puzzle import PuzzleState

def check_memory_limit(max_gb=4.0):
    """
    Function that constantly checks the memory usage for the overall program.
    A MemoryError will be raised if the memory limit (4.0 GB) is exceeded.
    This function was added due to the RAM constraints on my local machine.
    """
    process = psutil.Process(os.getpid())
    mem_usage_gb = process.memory_info().rss / (1024 ** 3)
    if mem_usage_gb > max_gb:
        raise MemoryError(
            f"Memory limit of {max_gb} GB has been exceeded. Script used {mem_usage_gb:.2f} GB of RAM "
            f"(Limit: {max_gb} GB). Stopping program to prevent system from crashing."
        )

def a_star_search(initial_state, heuristic_func_name="h2", max_frontier_size=2000000, max_ram_gb=4.0):
    """
    Perform A* Search algorithm on the given puzzle.
    """
    start_time = time.time()

    if heuristic_func_name == "h1":
        heuristic = lambda state: state.h1_misplaced()
    else:
        heuristic = lambda state: state.h2_manhattan()

    # Evaluation formula for A* search [f(n) = g(n) + g(n)] represented here
    counter = 0
    h_initial = heuristic(initial_state)
    frontier = [(initial_state.cost + h_initial, counter, initial_state)]

    # Track visited paths here
    visited_paths = {initial_state.board: initial_state.cost}

    max_frontier_reached = len(frontier)
    explored_count = 0

    while frontier:
        if explored_count % 5000 == 0:
            check_memory_limit(max_gb=max_ram_gb)

        if len(frontier) > max_frontier_size:
            raise MemoryError(
                f"Frontier size exceeds the max cap size of {max_frontier_size} states. "
                "Stopping search now."
            )

        max_frontier_reached = max(max_frontier_reached, len(frontier))

        current_f, _, current_state = heapq.heappop(frontier)

        # Was the goal ever reached? (Prob not bc limited RAM but it's fine)
        if current_state.is_goal():
            end_time = time.time()
            path =[]
            curr = current_state
            while curr.parent is not None:
                path.append(curr.move)
                curr = curr.parent
            path.reverse()

            return {
                "success": True,
                "path": path,
                "cost": current_state.cost,
                "explored_nodes_count": explored_count,
                "max_frontier": max_frontier_reached,
                "time_elapsed": end_time - start_time
            }
        
        explored_count += 1

        for neighbor in current_state.get_neighbors():
            if neighbor.board in visited_paths and visited_paths[neighbor.board] <= neighbor.cost:
                continue
            visited_paths[neighbor.board] = neighbor.cost
            counter += 1
            f_score = neighbor.cost + heuristic(neighbor)
            heapq.heappush(frontier, (f_score, counter, neighbor))

    return {
        "success": False,
        "explored_nodes_count": explored_count,
        "max_frontier": max_frontier_reached,
        "time_elapsed": time.time() - start_time
    }
    

