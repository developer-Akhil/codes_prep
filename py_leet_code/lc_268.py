from typing import List


class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        sum_to_be = n * (n + 1) / 2
        actual_sum = 0

        for num in nums:
            actual_sum += num

        return int(abs(sum_to_be - actual_sum))

print(Solution().missingNumber([0, 1]))


class Solution1:
    def missingNumber(self, nums: List[int]) -> int:

        nums_set = set(nums)

        n = len(nums)
        for i in range(0, n + 1):

            if i in nums_set:  # O(1)
                # if i in nums:         # O(n)
                continue
            else:
                return i
