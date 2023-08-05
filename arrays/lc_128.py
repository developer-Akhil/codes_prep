
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        result = 0

        for num in nums:


            if num -1 not in nums:

                length = 0

                while num + length in num_set:

                    length +=1

                result = max(length,result)

        return result

nums = [100, 4, 200, 1, 3, 2]
print(Solution().longestConsecutive(nums))


