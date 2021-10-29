import sys
from collections import deque

n, m = map(int, input().split())

maze = []
for _ in range(n):
    maze.append([j for j in map(int, sys.stdin.readline().strip('\n'))])

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = [[0] * m for _ in range(n)]
answer = [[0] * m for _ in range(n)]


def bfs(start_i, start_j):
    answer[start_i][start_j] = 1
    visited[start_i][start_j] = 1

    queue = deque()
    queue.append([start_i, start_j])

    while queue:
        v = queue.popleft()
        x, y = v[0], v[1]

        for i in range(4):
            _dx, _dy = x + dx[i], y + dy[i]
            if 0 <= _dx < n and 0 <= _dy < m and maze[_dx][_dy] == 1 and visited[_dx][_dy] == 0:
                visited[_dx][_dy] = 1
                queue.append([_dx, _dy])
                answer[_dx][_dy] = answer[x][y] + 1


bfs(0, 0)
print(answer[n - 1][m - 1])
