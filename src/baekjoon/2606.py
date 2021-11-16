# https://www.acmicpc.net/problem/2606
# 바이러스

from collections import deque

v = int(input())
e = int(input())

graph = [[0]*(v+1) for _ in range(v+1)]
visited = [0 for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1


def bfs(start):
    global answer
    q = deque()
    q.append(start)

    while q:
        item = q.popleft()
        visited[item] = 1
        answer += 1
        for j in range(v+1):
            if graph[item][j] and not visited[j] and j not in q:
                q.append(j)


answer = 0
bfs(1)
print(answer-1)








