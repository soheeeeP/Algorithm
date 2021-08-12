def solution(arr):
    start = 2
    lcm = []
    while True:
        if start > max(arr):
            break
        flag = False
        for x in range(len(arr)):
            if arr[x] % start == 0:
                flag = True
                arr[x] /= start

        if flag:
            lcm.append(start)
        else:
            start += 1

    answer = 1
    for x in lcm:
        answer *= x
    for x in arr:
        answer *= x

        return answer

if __name__ == "__main__":
    print(solution([2,6,12,14]))
    print(solution([2,6,8,14]))