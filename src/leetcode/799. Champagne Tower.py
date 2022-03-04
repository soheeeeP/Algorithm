class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [0] * (query_row + 1)
        dp[0] = poured

        for i in range(query_row):
            _dp = [0] * (query_row + 1)
            for j in range(0, i + 1):
                if dp[j] > 1:
                    _dp[j] += (dp[j] - 1) / 2
                    _dp[j + 1] += (dp[j] - 1) / 2
            dp = _dp

        return min(1.0, dp[query_glass])


if __name__ == '__main__':
    print(Solution().champagneTower(25, 6, 1))
    print(Solution().champagneTower(2, 0, 0))
    print(Solution().champagneTower(2, 1, 1))
    print(Solution().champagneTower(4, 2, 2))
    print(Solution().champagneTower(8, 3, 2))
    print(Solution().champagneTower(100000009, 33, 17))

