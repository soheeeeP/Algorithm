from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.firstIdx(nums, target), self.lastIdx(nums, target)]

    def firstIdx(self, nums: List[int], target: int):
        low, high, pos = 0, len(nums) - 1, -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                pos = mid
                high = mid - 1

        return pos

    def lastIdx(self, nums: List[int], target: int):
        low, high, pos = 0, len(nums) - 1, -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                pos = mid
                low = mid + 1

        return pos


if __name__ == '__main__':
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))
    print(Solution().searchRange([], 0))
    print(Solution().searchRange([1, 3], 1))
    print(Solution().searchRange([3, 3, 3], 3))
    print(Solution().searchRange([1, 3, 5, 5, 5, 5, 67, 123, 125], 5))
