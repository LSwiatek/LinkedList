from collections import deque

def bfs_maze(grid):
    n, m = len(grid), len(grid[0])
    start = (0, 0)
    target = (n-1, m-1)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q = deque([start])
    seen = set()
    seen.add(start)
    previous = {start: None}

    while q:
        current = q.popleft()
        if current == target:
            break

        for move in moves:
            next_row = current[0] + move[0]
            next_col = current[1] + move[1]
            next_position = (next_row, next_col)

            if 0 <= next_row < n and 0 <= next_col < m and grid[next_row][next_col] == ' ' and next_position not in seen:
                q.append(next_position)
                seen.add(next_position)
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
    "######",
    "# ## #",
    "#     ",
    "##### "
]

print(bfs_maze(grid))





