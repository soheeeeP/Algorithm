n = int(input())
dp = [0 for _ in range(3)]

dp[0] = 1
dp[1] = 2
for i in range(2, n):
    dp[i % 3] = (dp[(i - 1) % 3] + dp[(i - 2) % 3]) % 15746

print(dp[(n - 1) % 3])
