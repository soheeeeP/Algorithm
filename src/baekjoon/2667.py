import sys

n = int(input())

data = []
for _ in range(n):
    data.append([j for j in map(int, sys.stdin.readline().strip('\n'))])
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
visited = [[False] * n for _ in range(n)]


def dfs(nx, ny):
    global count
    visited[nx][ny] = True
    count += 1
    for t in range(4):
        _dx, _dy = nx + dx[t], ny + dy[t]
        if 0 <= _dx < n and 0 <= _dy < n and data[_dx][_dy] and visited[_dx][_dy] is not True:
            dfs(nx=_dx, ny=_dy)


section = []
for i in range(n):
    for j in range(n):
        if data[i][j] and visited[i][j] is not True:
            count = 0
            dfs(nx=i, ny=j)
            section.append(count)

section.sort()
print(len(section))
for _ in section:
    print(_)
