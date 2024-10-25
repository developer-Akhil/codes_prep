from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid + 1

            if nums[mid] < target:
                l = mid + 1

            else:
                r = mid - 1

        if l > r:
            print("There is no value is present")


nums = [-1, 0, 3, 5, 9, 12]
target = 0

print(Solution().search(nums, target))
