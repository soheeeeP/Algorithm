from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        _matrix = sum(matrix, [])
        low, high, pos = 0, len(_matrix), -1
        while low < high:
            middle = low + (high - low) // 2
            if _matrix[middle] == target:
                pos = middle
                break
            elif _matrix[middle] < target:
                low = middle + 1
            else:
                high = middle

        return False if pos == -1 else True


if __name__ == '__main__':
    print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 10))
    print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
