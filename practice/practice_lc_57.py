from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []

        for i in range(len(intervals)):

            if newInterval[1] < intervals[i][0]:

                result.append(newInterval)

                return result + intervals[i:]

            elif newInterval[0] > intervals[i][1]:

                result.append(intervals[i])

            else:

                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]

        result.append(newInterval)

        return result

""" new_inv[1] < inv[i][0] """
# intervals = [[2, 3], [3, 4]]
# newInterval = [0, 1]

""" elif new_inv[0] > inv[i][1]: """
# intervals = [[2, 3], [3, 4], [6, 7]]
# newInterval = [9, 10]

"""for else condition """
intervals = [[2, 3], [3, 4], [6, 7]]
newInterval = [4, 5]

print(Solution().insert(intervals, newInterval))