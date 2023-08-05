import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        heapq.heapify(minHeap)

        for num in nums:

            heapq.heappush(minHeap, num)

            print(minHeap)

            if len(minHeap) > k:
                heapq.heappop(minHeap)

                # print(element)

        return heapq.heappop(minHeap)


nums = [3, 2, 1, 5, 6, 4]

print(Solution().findKthLargest(nums, 2))
