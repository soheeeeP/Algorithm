from sys import stdin

n = int(input())
level = list(map(int, stdin.readline().split()))
dp = [0 for _ in range(n)]

cnt = 0
for i in range(n-1):
    if level[i] > level[i+1]:
        cnt += 1
    dp[i+1] = cnt


q = int(input())
for i in range(q):
    x, y = map(int, stdin.readline().split())
    print(dp[y-1]-dp[x-1])
