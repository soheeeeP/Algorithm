import sys

n = int(input())
data = []
for i in range(n):
    data.append([j for j in map(int, sys.stdin.readline().split())])

# data.sort(key=lambda x: x[1] - x[0])
data.sort(key=lambda x: (x[1], x[0]))

answer = 0
time = 0
for x in data:
    if time <= x[0]:
        time = x[1]
        answer += 1

print(answer)

