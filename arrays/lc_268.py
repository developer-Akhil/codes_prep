from typing import List


class Solution:

    def missingNumber(self, nums):
        l = len(nums)

        final = (1 + l) * l / 2

        for i in nums:
            final -= i

        return int(final)



""" Using Hashmap """


class SolutionHash:

    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        visited = set()

        for num in nums:
            visited.add(num)

        for i in range(0, n):

            if i not in visited:
                return i


print(SolutionHash().missingNumber([0, 1, 2, 4, 5, 6]))
