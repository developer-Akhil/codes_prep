from typing import List


class Solution:

    def merge(self, intervals: List[List[int]]) -> List:

        res = []
        sorted_in = sorted(intervals, key=lambda x: x[0])

        for interval in sorted_in:

            if res and interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)

        return res


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# intervals=[(3, 6), (5, 7), (6, 12), (10, 11), (10, 12)]

# new_list

# intervals=[(5, 7), (11, 116), (3, 4), (10, 12), (6, 12)]

# intervals=[[5, 7], [11, 116], [3, 4], [10, 12], [6, 12]]

print(Solution().merge(intervals))

