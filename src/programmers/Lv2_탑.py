def solution(heights):
    size = len(heights)
    answer = [0 for i in range(size)]

    for x in reversed(range(len(heights))):
        for y in range(0, x):
            if heights[x] < heights[y]:
                answer[x] = y + 1

    return answer


if __name__ == "__main__":
    print(solution([6, 9, 5, 7, 4]))
    print(solution([3, 9, 9, 3, 5, 7, 2]))
    print(solution([1, 5, 3, 6, 7, 6, 5]))
