# https://www.acmicpc.net/problem/2096
# 2096 내려가기

n = int(input())
arr = list(map(int, input().split()))
min_dp, max_dp = arr.copy(), arr.copy()

for i in range(1, n):
    arr = list(map(int, input().split()))
    val0 = min(min_dp[0] + arr[0], min_dp[1] + arr[0])
    val1 = min(min_dp[0] + arr[1], min_dp[1] + arr[1], min_dp[2] + arr[1])
    val2 = min(min_dp[1] + arr[2], min_dp[2] + arr[2])
    min_dp = [val0, val1, val2]

    val0 = max(max_dp[0] + arr[0], max_dp[1] + arr[0])
    val1 = max(max_dp[0] + arr[1], max_dp[1] + arr[1], max_dp[2] + arr[1])
    val2 = max(max_dp[1] + arr[2], max_dp[2] + arr[2])
    max_dp = [val0, val1, val2]

print(f'{max(max_dp)} {min(min_dp)}')

