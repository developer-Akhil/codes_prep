import sys
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []

        count = {}

        freq = [[] for i in range(0, len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        # print(count)
        # sys.exit()

        for key, val in count.items():
            freq[val].append(key)

        for i in range(len(freq) - 1, 0, -1):

            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        print(res)

        sys.exit()

print(Solution().topKFrequent([1,1,1,2,2,3],2))