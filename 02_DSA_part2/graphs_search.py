from collections import defaultdict, deque


# find if path exists in graph with DFS:
def valid_path_DFS(n: int, edges: list[int], source: int, destination: int) -> bool:
    if source == destination:
        return True

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    seen = set()
    seen.add(source)

    def dfs(i):
        if i == destination:
            return True

        for nei_node in graph[i]:
            if nei_node not in seen:
                seen.add(nei_node)
                if dfs(nei_node):
                    return True

        return False

    return dfs(source)


print(valid_path_DFS(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2))


# find if path exists in graph with BFS:
def valid_path_BFS(n: int, edges: list[int], source: int, destination: int) -> bool:
    if source == destination:
        return True

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    seen = set()
    seen.add(source)
    q = deque()
    q.append(source)

    while q:
        node = q.popleft()
        if node == destination:
            return True
        for nei_node in graph[node]:
            if nei_node not in seen:
                seen.add(nei_node)
                q.append(nei_node)

    return False


print(valid_path_BFS(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2))