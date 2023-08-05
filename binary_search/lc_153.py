from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1

        while l < r:

            mid = (l + r) // 2

            if nums[mid] > nums[r]:

                l = mid + 1

            else:
                r = mid
        return nums[l]


print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))
