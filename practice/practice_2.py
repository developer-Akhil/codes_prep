# nums = 6
#
# l = [[] for i in range(6 + 1)]
# print(l)

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []

        count = {}

        freq = [[] for i in range(len(nums))]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for key, value in count.items():
            freq[value].append(key)

        for i in range(len(freq) - 1, 0, -1):

            for j in freq[i]:

                res.append(j)

                if len(res) == k:
                    return res


# class Solution:
#     def topKFrequent(self, nums: List[int], k1: int) -> List[int]:
#
#         res = []
#
#         count = {}
#
#         freq = [[] for i in range(len(nums))]
#
#         for num in nums:
#             count[num] = count.get(num, 0) + 1
#
#         for k, v in count.items():
#             freq[v].append(k)
#
#         # print(freq)
#
#         for i in range(len(freq) - 1, 0, -1):
#
#             for j in freq[i]:
#
#                 res.append(j)
#
#                 if len(res) == k1:
#                     return res
# print(res)


print(Solution().topKFrequent([1, 1, 1, 2, 3, 3, 4], 2))

