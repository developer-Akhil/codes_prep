from typing import List


class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        new_nms = set()

        for num in nums:

            if num not in new_nms:

                new_nms.add(num)
            else:
                return True
        return False




nums = [1, 2, 3 ,4]

print(Solution().containsDuplicate(nums))
