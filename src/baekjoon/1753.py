import heapq
import sys

V, E = map(int, input().split())
start = int(input())

# graph = [[0] * (V+1) for _ in range(V+1)] : 메모리 초과
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([w, v])             # (가중치, 노드번호) 튜플을 graph[u]의 리스트에 추가

queue = []
distance = [float('inf') for _ in range(V+1)]
distance[start] = 0
heapq.heappush(queue, (0, start))       # 가중치, 노드번호
while queue:
    cur_weight, cur_node = heapq.heappop(queue)
    for weight, next_node in graph[cur_node]:
        new_weight = weight + cur_weight
        if new_weight < distance[next_node]:
            distance[next_node] = new_weight
            heapq.heappush(queue, (distance[next_node], next_node))

for i in range(1, len(distance)):
    if distance[i] == float('inf'):
        print('INF')
    else:
        print(distance[i])

