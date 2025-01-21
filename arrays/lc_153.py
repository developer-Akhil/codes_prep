from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        while l < r:

            if nums[l] < nums[r]:
                return nums[l]

            m = l + (r - l) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return nums[l]


print(Solution().findMin([3, 4, 5, 1, 2]))


# Code
# https://www.enjoyalgorithms.com/blog/minimum-in-sorted-and-rotated-array

# Videos
# https://www.youtube.com/watch?v=j3187M1P2Xg
