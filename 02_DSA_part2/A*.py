from collections import defaultdict
import heapq


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star_search(grid):
    m, n = len(grid), len(grid[0])
    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    open = [] #frontier
    closed = defaultdict(list) #came from

    start = grid[0][0]
    heapq.heappush(open, (0, start))
    finish = grid[m-1][n-1]

    cost = defaultdict(list)
    closed[start] = None
    cost[start] = 0

    while open:
        current = heapq.heappop(open)

        if current == finish:
            path = []
            while current in closed:
                path.append(current)
                current = closed[current]
            path.append(start)
            path.reverse()
            return path

        for nei in neighbors:
            neighbor = (current[0] + nei[0], current[1] + nei[1])

            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_cost = cost[current] + 1

                if neighbor not in cost or tentative_cost < cost[neighbor]:
                    closed[neighbor] = current
                    cost[neighbor] = tentative_cost
                    score = tentative_cost + heuristic(neighbor, finish)
                    heapq.heappush(open, (score, neighbor))

            return None


print(a_star_search([[1, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0]]))

