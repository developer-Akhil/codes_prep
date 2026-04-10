from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        n = len(nums)
        seen = set()

        duplicate = -1

        expected_sum = n * (n+1)//2

        actual_sum = 0

        for num in nums:

            if num in seen:

                duplicate = num
            seen.add(num)
            actual_sum += num

        missing = expected_sum - (actual_sum - duplicate)
        return [duplicate,missing]


# lst = [1,1]
lst = [1,2,2,4]
print(Solution().findErrorNums(lst))
