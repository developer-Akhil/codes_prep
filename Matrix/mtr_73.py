
from typing import List

# class Solution():
#
#     def setZeroes(self,matrix:List[List[int]]):
#
#         ROWS,COLS = len(matrix),len(matrix[0])
#         rowZero = False
#
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if matrix[r][c] == 0:
#                     matrix[0][c] = 0
#
#                     if r > 0:
#                         matrix[r][0] = 0
#                     else:
#                         rowZero = True
#
#         for i in range(1,ROWS):
#             for c in range(1,COLS):
#                 if matrix[0][r] == 0 or matrix[r][0] == 0:
#                     matrix[r][c]
#         if matrix[0][0] == 0:
#
#             for r in range(ROWS):
#                 matrix[r][0]=0
#
#         if rowZero:
#             for c in range(COLS):
#                 matrix[0][c]=0

class Solution:

    def setZeroes(self, matrix: List[List[int]]): #-> None:
        """
            Do not return anything, modify matrix in-place instead.
        """
        rLen,cLen=len(matrix),len(matrix[0])

        col=[1]*cLen

        for r in range(rLen):
            flag = 0  # flag=1 INDICATES CURRENT ROW CONTAINS 0
            for c in range(cLen):

                if matrix[r][c] == 0:
                    flag = 1
                    col[c] = 0

            if flag:  # flag=1 INDICATES CURRENT ROW CONTAINS 0, SET ENTIRE ROW TO 0
                matrix[r] = [0] * cLen

        '''
            col INDICATES WHICH COLUMN HAS 0,
            BELOW LOOP SET THE CORRESPONDING COLUMN 0

        '''

        for r in range(rLen):
            for c in range(cLen):
                if col[c] == 0:
                    matrix[r][c] = 0

        return matrix

matrix = [[1,1,1],[1,0,1],[1,1,1]]

print(Solution().setZeroes(matrix))

