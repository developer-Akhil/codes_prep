import sys
from typing import List

""" Smallest sum contiguous subarray -- GFG """
"""
Efficient Approach: Kadane’s Algorithm
Kadane’s Algorithm is an iterative dynamic programming algorithm. It calculates the maximum sum subarray ending at a particular
position by using the maximum sum subarray ending at the previous position. Follow the below steps to solve the problem.

Define two-variable currSum which stores maximum sum ending here and maxSum which stores maximum sum so far.
Initialize currSum with 0 and maxSum with INT_MIN.
Now, iterate over the array and add the value of the current element to currSum and check
If currSum is greater than maxSum, update maxSum equals to currSum.
If currSum is less than zero, make currSum equal to zero.
Finally, print the value of maxSum.

"""


def smallestSumSubarr(arr: List[int]):
    ans = sys.maxsize
    # ans = 'inf'
    sum_val = 0

    for i in range(0, len(arr) - 1):
        sum_val = min(arr[i], arr[i] + sum_val)

        ans = min(ans, sum_val)

    return ans


arr = [2, 6, 8, 1, -2,-4, 4]

# arr = [2, 6, 8, 1, 4]

print(smallestSumSubarr(arr))
