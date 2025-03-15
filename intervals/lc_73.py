from typing import List


class Solution:

    def set_zeroes(self, matrix: List[List[int]]) -> None:
        col0, rows, cols = 1, len(matrix), len(matrix[0])

        for i in range(0, rows):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(rows - 1, -1, -1):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0

        print(matrix)

        # def set_zeroes(self, matrix: List[List[int]]) -> None:
    #     rows, cols = len(matrix), len(matrix[0])
    
    #     row_zero = False
    
    #     for r in range(rows):
    #
    #         for c in range(cols):
    #
    #             if matrix[r][c] == 0:
    #                 matrix[0][c] = 0
    #
    #                 if r > 0:
    #                     matrix[r][0] = 0
    #                 else:
    #                     row_zero = True
    #
    #     for r in range(1, rows):
    #         for c in range(1, cols):
    #
    #             if matrix[0][r] == 0 or matrix[r][0] == 0:
    #                 matrix[r][c] = 0
    #
    #     if matrix[0][0] == 0:
    #         for r in range(rows):
    #             matrix[r][0] = 0
    #
    #     if row_zero:
    #         for c in range(cols):
    #             matrix[0][c] = 0


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

print(Solution().set_zeroes(matrix))

