from typing import List


class Solution:

    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if m * n != len(original):
            return []
        ans = []

        for i in range(0, m * n, n):
            ans.append(original[i:i + n])

        return ans


original = [1, 2, 3, 4]
m = 2
n = 2
print(Solution().construct2DArray(original, m, n))

