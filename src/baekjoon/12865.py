n, k = map(int, input().split())
w, v = [0 for _ in range(n)], [0 for _ in range(n)]

dp = [[0]*(k+1) for _ in range(n)]

for i in range(n):
    w[i], v[i] = map(int, input().split())

for i in range(n):
    for j in range(k+1):
        if j - w[i] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp)


dp = [0 for _ in range(k+1)]
for i in range(n):
    for j in range(k, 0, -1):
        if j - w[i] >= 0:
            dp[j] = max(dp[j], dp[j-w[i]] + v[i])
    print(dp)

