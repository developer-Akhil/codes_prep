from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        new_nums = set(nums)

        print(new_nums)
        print(sum(nums))
        print(sum(new_nums))

        return 2*sum(new_nums) - sum(nums)


print(Solution().singleNumber([2, 2, 1]))
