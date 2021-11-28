# https://www.acmicpc.net/problem/2003
# 2003 수들의 합 2

n, m = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, 0
answer = 0
while s <= n and e <= n:
    val = sum(arr[s:e])
    if val > m:
        s += 1
    else:
        if val == m:
            answer += 1
        e += 1


print(answer)

