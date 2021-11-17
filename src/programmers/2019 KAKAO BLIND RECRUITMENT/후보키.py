# https://programmers.co.kr/learn/courses/30/lessons/42890
# 후보키

import numpy as np
from itertools import combinations


def solution(relation):
    answer = 0
    row, col = np.shape(relation)[0], np.shape(relation)[1]
    attr = np.array(relation).T.tolist()

    key = []
    for i in range(1, col + 1):
        key.extend(combinations(range(col), i))

    key_set = []
    for k in key:
        a = [tuple([item[x] for x in k]) for item in relation]
        # axis = 0 if len(k) == 1 else 1
        # a = np.stack((attr[x] for x in k), axis=axis).tolist()
        if len(set(a)) == row:
            check = True
            for y in key_set:
                if set(y).issubset(k):
                    check = False
                    break
            if check:
                key_set.append(k)

    return len(key_set)


if __name__ == '__main__':
    solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
              ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]])
