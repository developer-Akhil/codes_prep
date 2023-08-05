# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#
#         for i in nums:
#
#             for j in nums:
#
#                 if i == j:
#                     return True
#         return False


#OR
#Time complexity : O(N)
#Space complexity : O(N)

class Solution(object):

    def containsDuplicate(self,nums):
        counter = set()
        for num in nums:
            if num not in counter:
                counter.add(num)
            else:
                return True

        return False


nums=[1,2,3,4,1]

print(Solution().containsDuplicate(nums))
