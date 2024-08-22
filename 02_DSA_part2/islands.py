from collections import defaultdict, deque


def count_islands(grid: list):
    m, n = len(grid), len(grid[0])

    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
            return
        else:
            grid[i][j] = 0
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i + 1, j + 1)
            dfs(i + 1, j - 1)
            dfs(i - 1, j)
            dfs(i - 1, j + 1)
            dfs(i - 1, j - 1)

    num_islands = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                num_islands += 1
                dfs(i, j)

    return num_islands


print(count_islands([[0,1,1,1,0,0,0],[0,0,1,1,0,1,0]]))
