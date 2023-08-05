import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]

        for n in nums:

            if curSum < 0:
                curSum = 0

            curSum = curSum + n
            maxSum = max(maxSum, curSum)
        return maxSum


# nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-1, 2, 3, 4]

print(Solution().maxSubArray(nums))
