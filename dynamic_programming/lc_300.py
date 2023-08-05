from typing import List


class Solution():

    def lengthOfLIS(self, nums: List[int]) -> int:

        len_num = len(nums)
        dp = [1] * len_num

        # Iterate through the array
        for i in range(1, len(nums)):
            # Iterate through the previous elements
            for j in range(i):
            # for j in range(i - 1, 0, -1):
                # If the current element is greater than the previous element, update the dp table
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # Return the maximum value in the dp table
        return max(dp)

# class Solution():
#
#     def lengthOfLIS(self, nums: List[int]) -> int:
#
#         LIS = [1] * len(nums)
#
#         for i in range(len(nums) - 1, -1, -1):
#
#             for j in range(i + 1, len(nums)):
#
#                 if nums[i] < nums[j]:
#                     LIS[i] = max(LIS[i], 1 + LIS[j])
#         return max(LIS)

nums = [0, 1, 0, 3, 2, 3]

# nums = [10,9,2,5,3,7,101,18]

print(Solution().lengthOfLIS(nums))
