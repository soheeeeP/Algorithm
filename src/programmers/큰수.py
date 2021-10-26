def solution(number, k):
    answer = ''

    size = len(number) - k - 1
    start_idx = 0

    while size >= 0:
        if number[start_idx] != '9':
            for x in range(start_idx + 1, len(number) - size):
                if number[start_idx] < number[x]:
                    start_idx = x
                    if number[x] == '9': break

        answer += number[start_idx]
        start_idx += 1
        size -= 1

    return answer


if __name__ == "__main__":
    solution("4177252841", 4)
