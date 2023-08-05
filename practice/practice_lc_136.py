from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_val = {}

        for i in nums:
            dict_val[i] = dict_val.get(i, 0) + 1

        for key, value in dict_val.items():

            if value == 1:
                return key

        # print(dict_val)

        # for i in dict_val.values():

        # return 0


nums = [4, 1, 2, 1, 2]
print(Solution().singleNumber(nums))
