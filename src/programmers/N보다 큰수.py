def solution(N, number):
    if number == N:
        return 1

    dp = [set() for _ in range(8)]
    for i, val in enumerate(dp, start=1):
        val.add(int(str(N)*i))

    answer = 0
    for i in range(1, 8):
        for j in range(i):
            for op1 in dp[j]:
                for op2 in dp[i-j-1]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 / op2)
        if number in dp[i]:
            print(dp)
            return i+1

    return -1


if __name__ == '__main__':
    print(solution(5, 12))
    print(solution(2, 11))
