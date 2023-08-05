from typing import List



class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        result = []
        for num in nums:

            if nums[abs(num) -1] < 0:

                result.append(abs(num))

            else:

                nums[abs(num) - 1] = nums[abs(num) -1] * -1

        return result

# nums = [4, 5, 2, 7, 8, 2, 5, 1]

nums = [4,3,2,7,8,2,3,1]

print(Solution().findDuplicates(nums))


""" Method 1 """


# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#
#         new_nms = set()
#         result = []
#         for num in nums:
#
#             if num not in new_nms:
#                 new_nms.add(num)
#
#             else:
#                 result.append(num)
#
#         return result


""" Method 2"""


# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#
#         new_nms = set()
#         result = []
#
#         for i in range(0,len(nums)-1):
#             for j in range(0,i):
#
#                 if nums[i] == nums[j]:
#
#                     result.append(nums[i])
#
#         return result


