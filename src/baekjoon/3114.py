from sys import stdin


def banana_prefix_sum(r, c, banana):
    global banana_sum
    for j in range(1, c):
        for i in range(0, r-1):
            banana_sum[i+1][j] = banana_sum[i][j] + banana[i][j]


def apple_prefix_sum(r, c, apple):
    global apple_sum
    for j in range(0, c):
        for i in range(r-2, -1, -1):
            apple_sum[i][j] = apple_sum[i+1][j] + apple[i+1][j]


def total_prefix_sum(r, c):
    global total_sum
    for i in range(r):
        for j in range(c):
            total_sum[i][j] = banana_sum[i][j] + apple_sum[i][j]


r, c = map(int, input().split())
banana, banana_sum = [[0]*c for _ in range(r)], [[0]*c for _ in range(r)]
apple, apple_sum = [[0]*c for _ in range(r)], [[0]*c for _ in range(r)]
total_sum = [[0]*c for _ in range(r)]
dp = [[0]*c for _ in range(r)]

for i in range(r):
    x = list(map(str, stdin.readline().split()))
    for j in range(c):
        val = int(x[j][1:])
        if x[j][0] == 'B':
            banana[i][j] = val
        else:
            apple[i][j] = val

apple_prefix_sum(r, c, apple)
banana_prefix_sum(r, c, banana)
total_prefix_sum(r, c)

for i in range(r):
    dp[i][0] = total_sum[i][0]

for j in range(1, c):
    for i in range(r):
        if i == 0:
            dp[i][j] = dp[i][j-1] + total_sum[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1] + total_sum[i][j], dp[i][j-1] + total_sum[i][j], dp[i-1][j] - apple[i][j])

print(dp[r-1][c-1])


