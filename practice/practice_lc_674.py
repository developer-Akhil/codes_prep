from typing import List


class Solution:

    def findLengthOfLCIS(self, nums: List[int]) -> int:

        maxL = 1
        leng = 1

        for num in range(1, len(nums)):

            if nums[num - 1] < nums[num]:
                leng += 1
                maxL = max(leng, maxL)
            else:
                maxL = max(leng, maxL)
                leng = 1

        return maxL


# nums = [1]
nums = [1, 3, 5, 0, 2, 7, 8, 9, 10]
# nums = [1, 3, 5, 7]
# nums = [1]
# nums = [2,2,2,2,2]
print(Solution().findLengthOfLCIS(nums))
