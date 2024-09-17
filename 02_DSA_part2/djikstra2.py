import heapq


def dijkstra(V, adj, S):
    min_weight = [float('inf')] * V
    min_weight[S] = 0
    min_dist = [(0, S)]  # (distance from source to node, node)

    while min_dist:
        current_dist, i = heapq.heappop(min_dist)

        for v, weight in adj[i]:
            distance = current_dist + weight

            if distance < min_weight[v]:
                min_weight[v] = distance
                heapq.heappush(min_dist, (distance, v))

    return min_weight


print(dijkstra(V=3, adj=[[(1, 1), (2, 6)], [(2, 3), (0, 1)], [(1, 3), (0, 6)]], S=2))
