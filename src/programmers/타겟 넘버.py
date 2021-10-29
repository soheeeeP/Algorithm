# https://programmers.co.kr/learn/courses/30/lessons/43165
# 타겟 넘버

def dfs(numbers, target, size):
    answer = 0
    if size == len(numbers):
        if sum(numbers) == target:
            return 1
        else:
            return 0

    answer += dfs(numbers, target, size+1)
    numbers[size] *= -1
    answer += dfs(numbers, target, size+1)
    return answer


def solution(numbers, target):
    _answer = dfs(numbers, target, 0)
    return _answer


if __name__ == "__main__":
    solution([1, 1, 1, 1, 1], 3)
