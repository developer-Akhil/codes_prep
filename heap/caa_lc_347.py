# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

# Example
# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2]

import collections
import heapq
import sys
from typing import List
from collections import  Counter
class Solution():

    def topKFrequent(self,nums:List[int],k:int) ->List[int]:


        res=[]
        i=0
        # dict = collections.Counter(nums)

        dict= {i: nums.count(i) for i in nums}

        print(dict)
        # sys.exit()
        #

        for val,count in dict.items():

            if len(res) < k:

                heapq.heappush(res,(count,val))             # res = [[1,3],[3,1]]
            else:
                heapq.heappush(res,(count,val))
                heapq.heappop(res)

        return [val for count,val in res]

# class Solution():
#
#     def topKFrequent(self,nums:List[int],k:int) -> List[int]:
#
#         c = Counter(nums)
#
#         c = sorted(c,key=lambda x:c[x],reverse=True)
#
#         return c[:k]



# class Solution():
#
#     def topKFrequent(self,nums:List[int],k:int) -> List[int]:
#
#         c = Counter(nums)
#         print(c)
#
#         c = [(-v,k) for k,v in c.items()]
#
#         print(c)
#         heapq.heapify(c)
#         #
#         print(c)
#         # sys.exit()
#         output=[]
#
#         for i in range(k):
#
#             item = heapq.heappop(c)
#             output.append(item[1])
#
#         return output

print(Solution().topKFrequent([3,1,1,1,2,2],2))