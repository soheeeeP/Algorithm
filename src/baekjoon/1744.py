n = int(input())
_pos = []
_neg = []
_one = []

for _ in range(n):
    num = int(input())
    if num <= 0:
        _neg.append(num)
    elif num > 1:
        _pos.append(num)
    else:
        _one.append(num)

_pos.sort(reverse=True)
_neg.sort()

answer = 0
for i in range(0, len(_pos) - 1, 2):
    answer += (_pos[i] * _pos[i + 1])
if len(_pos) % 2 != 0:
    answer += _pos[len(_pos) - 1]

for i in range(0, len(_neg) - 1, 2):
    answer += (_neg[i] * _neg[i + 1])
if len(_neg) % 2 != 0:
    answer += _neg[len(_neg) - 1]

answer += len(_one)
print(answer)


