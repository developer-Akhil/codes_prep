from typing import List


class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:

        visited = set()

        for i in nums:

            if i not in visited:

                visited.add(i)

            else:
                return False

        return True
        # dict_val = {}
        #
        # for i in range(0, len(nums) - 1):
        #
        #     if nums[i] in dict_val:
        #         return True
        #
        #     dict_val[nums[i]] = i
        #
        # return False


# class Solution:
#
#     def containsDuplicate(self, nums: List[int]) -> bool:
#
#         visited = set()
#
#         for i in nums:
#
#             if i in visited:
#                 return True
#
#             visited.add(i)
#         return False


print(Solution().containsDuplicate([1, 2, 3, 1]))
