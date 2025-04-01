from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:

                return mid

            elif nums[mid] >= nums[l]:

                if target < nums[mid] and target >= nums[l]:            # left side search
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target > nums[mid] and target <= nums[r]:            # right side search
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

nums = [4, 5, 6, 7, 0, 1, 2]
target = 6

print(Solution().search(nums, target))
