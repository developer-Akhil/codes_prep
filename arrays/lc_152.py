from typing import List


class Solution:

    def maxProduct(self, nums: List[int]) -> int:

        min_val, max_val, res = nums[0], nums[0], nums[0]

        for n in range(1, len(nums)):

            if nums[n] < 0:
                tmp = min_val

                min_val = max_val

                max_val = tmp

            max_val = max(nums[n], nums[n] * max_val)

            min_val = min(nums[n], nums[n] * min_val)

            res = max(max_val, res)

        return res

    # res = max(nums)
    # curMin, curMax = 1, 1
    #
    # for n in nums:
    #
    #     if n == 0:
    #         curMin, curMax = 1, 1
    #         continue
    #
    #     tmp = curMax * n
    #
    #     curMax = max(n * curMax, n * curMin, n)
    #
    #     curMin = min(tmp, n * curMin, n)
    #
    #     res = max(res, curMax)
    #
    # return res


print(Solution().maxProduct([2, 3, -2, 4]))

print(Solution().maxProduct([-2, 0, -1]))

print(Solution().maxProduct([-4, -3]))
