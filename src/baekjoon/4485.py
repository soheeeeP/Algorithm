import heapq
import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dijkstra():
    queue = []
    heapq.heappush(queue, (maze[0][0], 0, 0))
    distance[0][0] = 0

    while queue:
        cost, x, y = heapq.heappop(queue)
        if x == size - 1 and y == size - 1:
            print(f'Problem {idx}: {distance[x][y]}')
            return

        for i in range(4):
            _dx, _dy = dx[i] + x, dy[i] + y
            if 0 <= _dx < size and 0 <= _dy < size:
                new_cost = cost + maze[_dx][_dy]
                if new_cost < distance[_dx][_dy]:
                    distance[_dx][_dy] = new_cost
                    heapq.heappush(queue, (new_cost, _dx, _dy))


idx = 1
while True:
    size = int(input())
    if size == 0:
        exit()

    maze = [list(map(int, input().split())) for _ in range(size)]
    distance = [[sys.maxsize] * size for _ in range(size)]
    dijkstra()
    idx += 1
