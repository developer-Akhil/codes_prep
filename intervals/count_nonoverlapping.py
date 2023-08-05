from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        count=1

        for i in range(1,len(intervals)):

            #print(intervals[i - 1][1],intervals[i][0])
            if intervals[i-1][1] >= intervals[i][0]:        # if

                 count = count+1


        return count

#[1,3],[2,4],[5,6],[6,7]
intervals = [[1,2],[2,3],[4,5],[5,7]]

print(Solution().eraseOverlapIntervals(intervals))