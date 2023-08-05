# from typing import List
# class Solution:
#     def dfs(self, grid, r, c):
#         grid[r][c] = '0'
#         lst = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
#         for row, col in lst:
#             if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[row]) and grid[row][col] == '1':
#                 self.dfs(grid, row, col)
#
#     def numIslands(self, grid: List[List[str]]) -> int:
#         islands = 0
#         for r in range(len(grid)):
#             for c in range(len(grid[r])):
#                 if grid[r][c] == '1':
#                     self.dfs(grid, r, c)
#                     islands += 1
#         return islands

from typing import List
class Solution:

    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count


    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Solution().numIslands(grid)