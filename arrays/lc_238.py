from typing import List

""" videos https://www.youtube.com/watch?v=4W_-bfV-C3M """


class Solution:

    def productExceptsSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        ans = [1] * n

        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        rightProd = 1

        for i in range(n - 1, -1, -1):
            ans[i] = ans[i] * rightProd

            rightProd = rightProd * nums[i]

        return ans


print(Solution().productExceptsSelf([1, 2, 3, 4]))
