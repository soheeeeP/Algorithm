from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = nums.index(min(nums))
        nums.sort()

        low, high, pos = 0, len(nums), -1
        while low < high:
            middle = low + (high - low) // 2
            if nums[middle] == target:
                pos = (middle + pivot) % len(nums)
                break
            elif nums[middle] < target:
                low = middle + 1
            else:
                high = middle

        return pos


if __name__ == '__main__':
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 5))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
    print(Solution().search([1], 0))
