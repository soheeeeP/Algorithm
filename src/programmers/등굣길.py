# https://programmers.co.kr/learn/courses/30/lessons/42898
# 등굣길

def solution(m, n, puddles):
    dp = [[0] * (n+1) for _ in range(m+1)]
    for val in puddles:
        dp[val[0]][val[1]] = -1     # 갈 수 없는 길을 block 처리

    dp[1][0] = 1                    # 시작값 지정
    for i in range(1, m+1):
        for j in range(1, n+1):
            if dp[i][j] == -1:
                dp[i][j] = 0
            else:       # 갈 수 있는 길인 경우, 최단 경로의 경우의 수 계산
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    return dp[m][n]


if __name__ == '__main__':
    solution(3, 4, [[2, 2]])
    solution(2, 2, [])
    solution(3, 3, [])
    solution(3, 3, [[2, 2]])
    solution(3, 3, [[2, 3]])
    solution(3, 3, [[1, 3]])
    solution(3, 3, [[1, 3], [3, 1]])
    solution(3, 3, [[1, 3], [3, 1], [2, 3]])
    solution(4, 4, [[3, 2], [2, 4]])
    solution(100, 100, [])
    solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]])
    solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]])
