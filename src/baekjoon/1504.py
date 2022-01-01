import heapq
import sys

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([c, b])
    graph[b].append([c, a])
v1, v2 = map(int, input().split())


def dijkstra(s):
    global graph
    distance = [sys.maxsize for _ in range(n + 1)]
    distance[s] = 0

    queue = []
    heapq.heappush(queue, [0, s])
    while queue:
        cur_weight, cur_node = heapq.heappop(queue)
        for weight, new_node in graph[cur_node]:
            new_weight = weight + cur_weight
            if new_weight < distance[new_node]:
                distance[new_node] = new_weight
                heapq.heappush(queue, (distance[new_node], new_node))

    return distance


start = dijkstra(1)
# 경로를 쪼개서 (시작점 단위) 계산한 뒤 합 경로를 비교
_v1, _v2 = dijkstra(v1), dijkstra(v2)
answer = min(start[v1] + _v1[v2] + _v2[n], start[v2] + _v2[v1] + _v1[n])
print(answer if answer < sys.maxsize else -1)
