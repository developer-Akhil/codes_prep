from typing import List


class Solution:

    def insert(slef, inv: List[List[int]], new_inv: List[int]) -> List[List[int]]:

        res = []

        for i in range(len(inv)):

            if new_inv[1] < inv[i][0]:

                res.append(new_inv)
                return res + inv[i:]
            elif new_inv[0] > inv[i][1]:
                res.append(inv[i])
            else:
                new_inv = [min(new_inv[0], inv[i][0]), max(new_inv[1], inv[i][1])]

        res.append(new_inv)

        return res


# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [4,8]
# intervals = [[1, 3], [6, 9]]
# newInterval = [2, 5]

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
