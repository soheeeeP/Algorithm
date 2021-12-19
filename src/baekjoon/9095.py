t = int(input())
dp = [0] * 10
dp[0], dp[1], dp[2] = 1, 2, 4
for i in range(3, 10):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(t):
    x = int(input())
    print(dp[x - 1])
