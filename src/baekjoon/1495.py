# https://www.acmicpc.net/problem/1495
# 1495 기타리스트

n, s, m = map(int, input().split())
volume = list(map(int, input().split()))

dp = [set(), set()]
dp[0].add(s)

for i, v in enumerate(volume):
    if len(dp[i % 2]) == 0:
        print(-1)
        exit()
    dp[(i + 1) % 2] = set()
    for p in dp[i % 2]:
        if 0 <= p + v <= m:
            dp[(i + 1) % 2].add(p + v)
        if 0 <= p - v <= m:
            dp[(i + 1) % 2].add(p - v)
if len(dp[n % 2]) == 0:
    answer = -1
else:
    answer = max(dp[n % 2])
print(answer)
