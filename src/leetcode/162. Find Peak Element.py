from typing import List


class Solution:
    # binary search (이진탐색)
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] >= nums[m+1]:
                r = m
            else:
                l = m + 1
        return l


if __name__ == '__main__':
    print(Solution().findPeakElement([1, 2]))
    print(Solution().findPeakElement([1, 2, 3, 1]))
    print(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]))
