def solution(word):
    key = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}

    cnt = 1
    for i in range(4):
        cnt = cnt * 5 + 1

    answer = len(word)
    for w in word:
        answer += key[w] * cnt
        cnt //= 5

    return answer

