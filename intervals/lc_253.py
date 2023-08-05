#Type: Medium
#Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei),
# find the minimum number of conference rooms required.

# videos : https://www.youtube.com/watch?v=FdzJmTCVyJU
# website: zhenyu0519.github.io/2020/07/13/lc253/

# Input:  [[0, 30],[5, 10],[15, 20]]
# Output: 2

# Input:  [[7,10],[2,4]]
# Output: 1

# sorted = O(nlogn) + O(n) = O(nlogn)
input=[[5, 10],[15, 20],[0, 30]]

class Solution():               # O(nlogn)
   def minMeetingRooms(self,intervals):

     start = sorted([i[0] for i in intervals])  # [0,5,15]
     end = sorted([i[1] for i in intervals])    # [10,20,30]

     res,count=0,0                              # res=2
     s,e=0,0

     while s < len(intervals):

         if start[s] < end[e]:                  # start[0] < end[0] | 0 < 10 , start[1] < end[0] | 5 < 10, start[2] < end[1] | 15 < 10 | start[2] < end[1] | 15 < 20
             s +=1                              # s =3
             count +=1                          # count =2
         else:
             e +=1                              # e=1
             count -=1                          # count = 1
         res=max(res,count)                     # res=max(0,1)| 1 , max(1,2)| 2   max(2,1) | 2

     return res

# Using Heap

from typing import List
import heapq

# class Solutions():
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         size = len(intervals)
#         if size <= 1: return size
#         heap = []
#         for interval in sorted(intervals):
#             if heap and interval[0] >= heap[0]:
#                 heapq.heappushpop(heap, interval[1])
#             else:
#                 heapq.heappush(heap, interval[1])
#         return len(heap)
#
# intervals=[[0,30],[5,10],[15,20]]
# print(Solutions().minMeetingRooms(intervals))