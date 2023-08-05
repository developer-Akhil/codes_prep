from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:

                if nums[l] <= target and target < nums[mid]:  # this for left
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                if target <= nums[r] and target > nums[mid]:  # this for right
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
print(Solution().search(nums, 6))
