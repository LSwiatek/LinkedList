from collections import defaultdict


def canFinish(numcourses: int, prerequisites: list) -> bool:
    g = defaultdict(list)
    courses = prerequisites
    for a, b in courses:
        g[a].append(b)

    UNVISITED = 0
    VISITING = 1
    VISITED = 2
    states = [UNVISITED] * numcourses

    def dfs(node):
        state = states[node]
        if state == VISITED:
            return True
        elif state == VISITING:
            return False

        states[node] = VISITING

        for nei in g[node]:
            if not dfs(nei):
                return False

        states[node] = VISITED
        return True

    for i in range(numcourses):
        if not dfs(i):
            return False

    return True


print(canFinish(numcourses=2, prerequisites=[[1, 0], [0, 1]]))
