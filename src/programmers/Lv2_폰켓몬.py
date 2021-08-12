def solution(nums):
    answer = 0
    length = len(nums) // 2
    nums_set = list(set(nums))

    for x in nums_set:
        if answer < length:
            answer += 1

    return answer


if __name__ == "__main__":
    print(solution([3, 1, 2, 3]))
    print(solution([3, 3, 3, 2, 2, 4]))
    print(solution([3, 3, 3, 2, 2, 2]))
