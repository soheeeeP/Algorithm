# https://www.acmicpc.net/problem/2643
# 2643 색종이 올려놓기

n = int(input())

paper = []
for i in range(n):
    x, y = map(int, input().split())
    paper.append([x, y]) if x < y else paper.append([y, x])
paper.sort()

dp = [0 for _ in range(n)]
for i in range(n):
    dp[i] = 1
    for j in range(0, i):
        if paper[i][0] >= paper[j][0] and paper[i][1] >= paper[j][1] and dp[j]+1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))
