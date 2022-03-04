from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i-2]:
                dp[i] = dp[i - 1] + 1

        return sum(dp)


if __name__ == '__main__':
    print(Solution().numberOfArithmeticSlices([1, 2, 3, 5, 6, 7]))
    print(Solution().numberOfArithmeticSlices([1, 2, 3, 4]))
