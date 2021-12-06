import bisect

x = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]
check = []

for i in range(x):
    if arr[i] > dp[-1]:
        check.append(len(dp))
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]
        check.append(idx)

print(len(dp))

idx = len(dp) - 1
i = len(check) - 1
answer = []
while idx >= 0:
    if check[i] == idx:
        answer.append(arr[i])
        idx -= 1
    i -= 1

answer.reverse()
print(*answer)
