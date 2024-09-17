import heapq


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star_maze(grid):
    n, m = len(grid), len(grid[0])
    start = (0, 0)
    target = (n-1, m-1)
    passed_dist = {start: 0}
    dist_to_target = {start: heuristic(start, target)}

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    open_set = []
    heapq.heappush(open_set, (0, start))
    previous = {start: None}

    while open_set:
        dist_score, current = heapq.heappop(open_set)
        if current == target:
            break

        for move in moves:
            next_row = current[0] + move[0]
            next_col = current[1] + move[1]
            next_position = (next_row, next_col)

            if 0 <= next_row < n and 0 <= next_col < m and grid[next_row][next_col] == ' ':
                temporary_passed_dist = passed_dist[current] + 1

                if next_position not in passed_dist or temporary_passed_dist < passed_dist[next_position]:
                    passed_dist[next_position] = temporary_passed_dist
                    dist_to_target[next_position] = temporary_passed_dist + heuristic(next_position, target)
                    heapq.heappush(open_set, (dist_to_target[next_position], next_position))
                    previous[next_position] = current
    path = []
    at = target
    while at is not None:
        path.append(at)
        at = previous[at]

    path.reverse()

    return path if path[0] == start else []


grid = [
    "  ####",
    "#    #",
    "# ## #",
    "# ## #",
    "#     ",
    "##### "
]

print(a_star_maze(grid))





