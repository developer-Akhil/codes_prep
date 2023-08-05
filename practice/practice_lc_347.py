""" 347. Top K Frequent Elements """

from sys import exit
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[]] * (len(nums) + 1)

        freq_dict = {}
        # freq = [[] for i in range(0,len(nums) + 1)]
        result = []

        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        for key, value in freq_dict.items():
            freq[value].append(key)

        for i in range(len(freq) - 1, 0, -1):

            for j in freq[i]:

                result.append(j)

                if len(result) == k:
                    return result


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution().topKFrequent(nums, k))
