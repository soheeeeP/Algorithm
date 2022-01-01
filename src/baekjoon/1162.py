import sys
import heapq


def dijkstra():
    global graph, k

    queue = []
    heapq.heappush(queue, [0, 1, 0]) # (가중치, 노드, k값)
    distance = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    distance[1][0] = 0

    while queue:
        cur_weight, cur_node, cur_k = heapq.heappop(queue)
        if distance[cur_node][cur_k] < cur_weight:
            continue

        for weight, next_node in graph[cur_node]:
            new_weight = weight + cur_weight
            if new_weight < distance[next_node][cur_k]:
                distance[next_node][cur_k] = new_weight
                heapq.heappush(queue, [new_weight, next_node, cur_k])
            if cur_k < k and cur_weight < distance[next_node][cur_k + 1]:
                distance[next_node][cur_k + 1] = cur_weight
                heapq.heappush(queue, [cur_weight, next_node, cur_k + 1])

    return distance


n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, weight = map(int, sys.stdin.readline().split())
    graph[a].append([weight, b])
    graph[b].append([weight, a])

d = dijkstra()
print(min(d[-1]))
