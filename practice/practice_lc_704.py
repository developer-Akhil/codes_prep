from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:

                return nums[mid]

            elif nums[mid] < target:

                l = mid + 1

            else:
                r = mid - 1


nums = [-1, 0, 3, 5, 9, 12]
target = 12


print(Solution().search(nums, target))
