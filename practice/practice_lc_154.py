from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:

            mid = (l + r) // 2

            if nums[mid] > nums[r]:

                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r = r - 1

        return nums[l]


nums = [3,3,3, 3, 3, 4, 1, 2, 3]

# nums = [2,2,2,0,1]
# nums = [3, 4, 5, 1, 2]

print(Solution().findMin(nums))
