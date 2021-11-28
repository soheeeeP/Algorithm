# https://www.acmicpc.net/problem/1484
# 1484 다이어트

g = int(input())

answer = []
end, start = 1, 1
while True:
    val = end**2 - start**2
    if val > g:
        if end - start == 1:
            break
        else:
            start += 1
    else:
        if val == g:
            answer.append(end)
        end += 1

if len(answer) == 0:
    print(-1)
    exit()

for x in answer:
    print(x)
