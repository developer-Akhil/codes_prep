from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        count = 0
        sorted_invl = sorted(intervals, key=lambda x: x[0])

        end_prev = intervals[0][1]

        for s, e in sorted_invl[1:]:

            if s >= end_prev:

                end_prev = e

            else:
                count += 1

                end_prev = min(e, end_prev)

        return count


# intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]

# intervals = [[1,2],[1,2],[1,2]]

# intervals = [[1,2],[2,3]]

intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]

print(Solution().eraseOverlapIntervals(intervals))
