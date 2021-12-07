def solution(triangle):
    size = len(triangle)
    dp = [[0] * (i+1) for i in range(size)]
    dp[0][0] = triangle[0][0]

    for i in range(size-1):
        for j in range(i+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + triangle[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1])

    return max(dp[size-1])


if __name__ == '__main__':
    solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
