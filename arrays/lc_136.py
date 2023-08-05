from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        map_val = {}

        for i in nums:

            if i not in map_val:
                map_val[i] = 1
            else:
                map_val[i] += 1

        print(map_val.values())
        for i in map_val:

            if map_val[i] == 1:
                return i

print(Solution().singleNumber([4,1,2,1,2]))