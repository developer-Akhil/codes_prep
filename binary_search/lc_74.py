from typing import List

""" Brute Force approach"""


# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#
#         for i in range(0, len(matrix) - 1):
#
#             for j in range(0, len(matrix[i]) - 1):
#
#                 if matrix[i][j] == target:
#                     return True
#
#         return False


# Time Complexity O(m*n)
#
# Space Complexity O(1)

class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int):

        if not matrix: return False

        n = len(matrix[0])
        m = len(matrix)

        l, r = 0, (n * m) - 1

        while l <= r:

            mid = (l + r) // 2

            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3

print(Solution().searchMatrix(matrix, target))
