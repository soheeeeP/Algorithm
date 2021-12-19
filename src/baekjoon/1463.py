# https://www.acmicpc.net/problem/1463
# 1463 1로 만들기

n = int(input())
if n == 1:
    print(0)
    exit()

dp = [[n], []]
idx = 0
answer = n
while True:
    for x in dp[idx % 2]:
        dp[(idx + 1) % 2].append(x - 1)
        if x % 3 == 0:
            dp[(idx + 1) % 2].append(x // 3)
        if x % 2 == 0:
            dp[(idx + 1) % 2].append(x // 2)
    if 1 in dp[(idx + 1) % 2]:
        answer = idx + 1
        break
    dp[idx % 2] = []
    idx += 1

print(answer)
