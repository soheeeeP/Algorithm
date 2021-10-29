# https://www.acmicpc.net/problem/1260
# DFS와 BFS

from collections import deque

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1


def dfs(start, visited):
    visited[start] = 1
    print(start, end=' ')

    for w in range(1, len(graph[start])):
        if graph[start][w] == 1 and visited[w] != 1:
            dfs(w, visited)


def bfs(start, visited):
    visited[start] = 1
    queue = deque()
    queue.append(start)

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for w in range(1, len(graph[start])):
            if graph[v][w] == 1 and visited[w] != 1:
                visited[w] = 1
                queue.append(w)


dfs(start=v, visited=[0 for _ in range(n+1)])
print()
bfs(start=v, visited=[0 for _ in range(n+1)])
