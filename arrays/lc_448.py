from typing import List


class Solution:

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        res = []

        for num in nums:

            if nums[abs(num) - 1] < 0:
                continue

            nums[abs(num) - 1] *= -1

        for idx in range(0, len(nums)):

            if nums[idx] > 0:
                res.append(idx + 1)

        return res


print(Solution().findDisappearedNumbers([0, 1, 2, 3, 4, 5, 5, 7]))
