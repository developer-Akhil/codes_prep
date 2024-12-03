from typing import List


class Solution:

    def rob(self, nums: List[int]):
        r1, r2 = 0, 0

        for n in nums:
            t = max(n + r1, r2)

            r1 = r2
            r2 = t

        return r2


# nums = [1, 2, 3, 1]
nums = [2, 7, 9, 3, 1]
print(Solution().rob(nums))

