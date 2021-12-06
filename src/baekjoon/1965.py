from sys import stdin

n = int(input())
box = list(map(int, stdin.readline().split()))
dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if box[j] < box[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp)+1)
