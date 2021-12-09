# https://www.acmicpc.net/problem/2293
# 동전1

import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))
coin.sort()

dp = [0] * 10001
dp[0] = 1
for val in coin:
    for i in range(val, k+1):
        dp[i] += dp[i-val]
print(dp[k])

