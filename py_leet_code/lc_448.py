from typing import List


class Solution:

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:

            if nums[abs(num) - 1] < 0:

                continue
            else:
                nums[abs(num) - 1] *= -1

        for idx in range(0, len(nums)):
            if nums[idx] > 0:
                res.append(idx + 1)

        return res


class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        res = []
        nums_set = set(nums)

        print(nums_set)

        for i in range(1, len(nums) + 1):

            if i in nums_set:
                continue

            else:
                res.append(i)

        return res


print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
