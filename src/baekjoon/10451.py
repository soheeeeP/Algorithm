import sys
sys.setrecursionlimit(10**7)


def cycle(v, data, visited):
    visited[v] = 1
    if visited[data[v-1]] == 1:
        return True
    return cycle(v=data[v-1], data=data, visited=visited)


T = int(input())
for t in range(T):
    n = int(input())
    data = list(map(int, sys.stdin.readline().split()))

    visited = [0 for _ in range(n + 1)]
    answer = 0
    for i in range(1, n + 1):
        if visited[i] == 0:
            if cycle(v=i, data=data, visited=visited):
                answer += 1

    print(answer)
