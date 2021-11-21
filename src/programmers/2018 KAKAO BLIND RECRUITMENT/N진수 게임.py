# https://programmers.co.kr/learn/courses/30/lessons/17687
# 2018 KAKAO BLIND RECRUITMENT [3차] n진수 게임

def solution(n, t, m, p):
    answer = ''

    max_len = m * t
    notation = '0'
    num = 1
    data = {i: format(i, 'x').upper() for i in range(n)}

    while True:
        if len(notation) >= max_len:
            break
        x = num
        base_x = ''
        while x > 0:
            base_x += str(data[x % n])
            # base_x += str(x % n)
            x //= n
        _base_x = ''.join(reversed(base_x))
        notation += _base_x
        num += 1

    for i in range(p, max_len+1, m):
        answer += notation[i - 1]

    return answer


if __name__ == '__main__':
    solution(2, 4, 2, 1)
    solution(16, 16, 2, 1)
    solution(16, 16, 2, 2)
