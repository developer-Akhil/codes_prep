from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        result = []

        for num in nums:

            if nums[abs(num) - 1] < 0:

                continue


            else:

                nums[abs(num) - 1] = nums[abs(num) - 1] * -1

        print(nums)
        for num in range(0, len(nums) - 1):

            if nums[num] > 0:
                result.append(num+1)

        return result


nums = [4, 3, 2, 7, 8, 2, 3, 1]

print(Solution().findDisappearedNumbers(nums))
