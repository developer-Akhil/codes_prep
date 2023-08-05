from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix: return False

        n = len(matrix[0])

        m = len(matrix)

        l, r = 0, (m * n) - 1

        while l <= r:

            mid = (l + r) // 2

            if matrix[mid // n][mid % n] == target:

                return True

            elif matrix[mid // n][mid % n] < target:

                l = m + 1

            else:
                r = m - 1

        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]

target = 3

print(Solution().searchMatrix(matrix,target))