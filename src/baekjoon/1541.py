data = input()

answer = 0
# 연산할 값이 남아있을때까지 계산
while data:
    # 수식에 더하기 연산만 있는 경우, 덧셈만 수행하고 바로 return
    if '-' not in data:
        num = [i for i in map(int, data.split('+'))]
        answer += sum(num)
        break

    for x in reversed(range(len(data))):
        if data[x] == '-':
            _data = data[x+1:]
            data = data[:x]
            break
    num = [i for i in map(int, _data.split('+'))]
    answer -= sum(num)

print(answer)
