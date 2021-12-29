# https://www.acmicpc.net/problem/2655
# 2655 가장 높은 탑 쌓기

n = int(input())

data = [[0,0,0,0]]
for i in range(n):
    # [밑면의 넓이(size), 벽돌의 높이(h), 벽돌의 무게(w)]
    size, height, weight = map(int, input().split())
    data.append([i+1, size, height, weight])
data.sort(key=lambda x: x[1])

dp = [0] * (n+1)
for i in range(1, n+1):
    for j in range(0, i):
        if data[i][3] > data[j][3]:
            dp[i] = max(dp[i], dp[j] + data[i][2])

height = max(dp)
idx = dp.index(height)
result = []
while idx != 0:
    if height == dp[idx]:
        result.append(data[idx][0])
        height -= data[idx][2]
    idx -= 1

result.reverse()
print(len(result))
for r in result:
    print(r)