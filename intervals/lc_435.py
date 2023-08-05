from typing import List


class Solution():

    def eraseOverlapIntervals(self, intervals: List[List[int]]):

        intervals.sort()

        # [[1, 2], [1, 3], [2, 3], [3, 4]]
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:

            if start >= prevEnd:
                prevEnd = end

            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]

print(Solution().eraseOverlapIntervals(intervals))
