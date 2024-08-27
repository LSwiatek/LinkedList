from collections import defaultdict
import heapq


def djikstra(times: list, n: int, k: int):
    graph = defaultdict(list)
    for u, v, time in times:
        graph[u].append((v, time))

    min_times = {}
    min_dist = [(0, k)]  # (distance from source to node, node)

    while min_dist:
        time_k_to_i, i = heapq.heappop(min_dist)
        if i in min_times:
            continue

        min_times[i] = time_k_to_i
        for nei, nei_time in graph[i]:
            if nei not in min_times:
                heapq.heappush(min_dist, (time_k_to_i + nei_time, nei))

    if len(min_times) == n:
        return max(min_times.values())
    else:
        return -1


print(djikstra(times=[[1, 2, 1]], n=2, k=1))
