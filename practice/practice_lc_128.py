from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        set_nums = set(nums)
        result = 0

        for num in nums:

            if num - 1 not in nums:

                length = 0

                while num + length in set_nums:
                    length += 1

                result = max(result, length)

        return result


nums = [100, 4, 200, 1, 3, 2]
print(Solution().longestConsecutive(nums))
