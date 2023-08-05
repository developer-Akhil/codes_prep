from typing import List


class Solution:

    def maxProduct(self, nums: List[int]) -> int:

        res = nums[0]
        mx = nums[0]
        mn = nums[0]

        for i in range(1, len(nums)):

            if nums[i] < 0:
                mx, mn = mn, mx

            mx = max(nums[i], mx * nums[i])
            mn = min(nums[i], mn * nums[i])

            res = max(res, mx)

        return res


nums = [2, 3, -2, 4]

print(Solution().maxProduct(nums))
