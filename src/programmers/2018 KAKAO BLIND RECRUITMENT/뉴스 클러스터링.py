# https://programmers.co.kr/learn/courses/30/lessons/17677
# 2018 KAKAO BLIND RECRUITMENT 뉴스 클러스터링

import re


def solution(str1, str2):
    if len(str1) == 0 and len(str2) == 0:
        return 0

    _str1, _str2 = [], []
    pattern = '[a-zA-z]{2}'

    for i in range(len(str1) - 1):
        s = str1[i:i + 2]
        if re.match(pattern, s) and '_' not in s:
            _str1.append(s.upper())

    for i in range(len(str2) - 1):
        s = str2[i:i + 2]
        if re.match(pattern, s) and '_' not in s:
            _str2.append(s.upper())

    _str1_size = len(_str1)
    _str2_size = len(_str2)

    data = []
    for s in _str1:
        if s in _str2:
            data.append(s)
            _str2.remove(s)
    intersection = len(data)

    # check_1, check_2 = len([x for x in _str1 if x in _str2]), len([x for x in _str2 if x in _str1])
    # intersection = min(check_1, check_2)

    answer = int(intersection / (_str1_size + _str2_size - intersection) * 65536)
    print(answer)

    return answer


if __name__ == '__main__':
    solution("aaabb", "aabbb")
    solution("FRANCE", "french")
    solution("handshake", "shake hands")
    solution("aa1+aa2", "AA12")
    solution("E=M*C^2", "e=m*c^2")
    solution("aa+aa+bb+bb", "AAAA+BBBB")
