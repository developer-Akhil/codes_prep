from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict_val = {}

        for i in range(len(nums)):

            val = target - nums[i]

            if nums[i] not in dict_val:

                dict_val[val] = i
            else:

                return [i, dict_val[nums[i]]]


# class Solution:
#
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#
#         dict_val = {}
#
#         for i in range(0, len(nums)):
#
#             diff = target - nums[i]
#
#             if nums[i] in dict_val:
#
#                 return [dict_val[nums[i]], i]
#
#             else:
#                 dict_val[diff] = i
#
#         return []


nums = [1, 5, 7, 2, 8]
target = 10

print(Solution().twoSum(nums, target))

# class Solution:
#
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#
#         dict_val = {}
#         for num in range(0, len(nums)):
#             val = target - nums[num]
#
#             if nums[num] not in dict_val:
#
#                 dict_val[val] = num
#
#             else:
#                 return [dict_val[nums[num]], num]
#
#         return []
