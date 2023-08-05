from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict_var = {}

        for i in range(0, len(nums)):

            complement = target - nums[i]

            if complement in dict_var:
                return [i, dict_var[complement]]

            dict_var[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9

print(Solution().twoSum(nums, 9))
