import math

n = int(input())
data = list(map(int, input().split()))
B, C = map(int, input().split())

_data = data
for i in range(n):
    if data[i] >= B:
        _data[i] -= B
    else:
        _data[i] = 0
answer_b = n

answer_a = 0
for x in _data:
    answer_a += math.ceil(x/C)

print(answer_a+answer_b)