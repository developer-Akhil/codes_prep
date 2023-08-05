from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1

        while l < r:

            mid = (l + r)//2

            if nums[mid] > nums[r]:

                l = mid + 1

            else:
                r = mid
        return nums[l]



print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))
    # def findMin(self, nums: List[int]) -> int:
    #
    #     l, r = 0, len(nums) - 1
    #
    #     while l < r:
    #
    #         if nums[l] < nums[r]:
    #             return nums[l]
    #
    #         m = l + (r - l) // 2
    #
    #         if nums[m] > nums[r]:
    #
    #             l = m + 1
    #         else:
    #             r = m
    #
    #     return nums[1]

    # def findMin(self, nums: List[int]) -> int:
    #
    #     n = len(nums)
    #
    #     l, r = 0, n - 1
    #
    #     while l < r:
    #
    #         mid = (l + r) // 2
    #
    #         if nums[mid] > nums[r]:
    #
    #             l = mid + 1
    #
    #         else:
    #             r = mid
    #
    #     return nums[l]

