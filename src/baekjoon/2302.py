# https://www.acmicpc.net/problem/2302
# 극장 좌석

n = int(input())
m = int(input())

dp = [0] * (n+1)
dp[0], dp[1] = 1, 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

if m == 0:
    print(dp[n])
    exit()

answer = 1
idx = 0
for i in range(m):
    x = int(input()) - 1
    answer *= dp[x - idx]
    idx = x + 1
answer *= dp[n - x - 1]
print(answer)
