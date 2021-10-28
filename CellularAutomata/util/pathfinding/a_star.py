import numpy as np
from CellularAutomata.util.rules.Rules import Rules


def a_star(maze):
    def heuristic(goal, pos):
        return abs(goal[0] - pos[0]) + abs(goal[1] - pos[1])

    def reconstruct_path(came_from, current):
        def is_in(list, item):
            for row in list:
                for ob in row:
                    if ob == item:
                        return True
            return False

        total_path = [current]
        first = True
        while first or is_in(came_from, current):
            first = False
            current = came_from[current[0]][current[1]]
            if current is None:
                return total_path
            if (current[0], current[1]) != maze.start and (current[0], current[1]) != maze.goal:
                if maze.grid[current[1]][current[0]] == 1:
                    maze.grid[current[1]][current[0]] = 5
                else:
                    maze.grid[current[1]][current[0]] = 4
            total_path.insert(0, current)
        return total_path

    open_set = [maze.start]
    closed_set = []

    # TODO: refactor these to store values in a 1D array and index = pixel index
    g_score = np.array([np.inf for _ in range(maze.cols * maze.rows)])
    g_score[(maze.start[0])][maze.start[1]] = 0

    came_from = [[None for _ in range(maze.cols)] for _ in range(maze.rows)]
    f_score = [[np.inf for _ in range(maze.cols)] for _ in range(maze.rows)]
    f_score[maze.start[0]][maze.start[1]] = heuristic(maze.goal, maze.start)

    while len(open_set) > 0:
        open_set.sort(key=lambda node: f_score[node[0]][node[1]])
        curr_tuple = open_set[0]
        curr_pos = curr_tuple

        # goal found
        if maze.goal == curr_pos:
            return reconstruct_path(came_from, curr_tuple)

        open_set = open_set[1:]
        closed_set.append(curr_tuple)
        # loop over all valid neighbors
        neighbors = maze.get_neighbors(curr_pos[0], curr_pos[1])
        for neighbor in neighbors:
            if neighbor in closed_set:
                continue
            row = neighbor[0]
            col = neighbor[1]
            score = g_score[curr_pos[0]][curr_pos[1]] + 1
            if score < g_score[row][col]:
                came_from[row][col] = curr_tuple
                g_score[row][col] = score
                f_score[row][col] = g_score[row][col] + heuristic(maze.goal, neighbor)
                if neighbor not in open_set:
                    open_set.append(neighbor)
    print("No path found")
    return []
