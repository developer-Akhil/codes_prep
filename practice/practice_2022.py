from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        result = []
        if m * n != len(original):
            return result

        for i in range(0, m * n, n):
            result.append(original[i:i + n])

        return result


original = [1, 2, 3, 4]
m, n = 2, 2

print(Solution().construct2DArray(original, m, n))
