from typing import List

""" Carl Gauss missing number formula """
""" we can find the "missing number" by finding the Gaussian Sum of the numbers, 
finding the actual sum of the numbers, and returning the difference. 

sum = (n * (n + 1)) / 2

missing number = (sum of actual number) - sum
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        cal_missing_nm = n * (n + 1) / 2

        sum_nums = 0
        for i in nums:
            sum_nums += i

        print(sum_nums)
        print(cal_missing_nm)
        return int(cal_missing_nm) - sum_nums


# nums = []

nums = [9,6,4,2,3,5,7,0,1]

print(Solution().missingNumber(nums))
