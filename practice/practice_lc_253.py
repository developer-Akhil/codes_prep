from typing import List


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    # [[0, 30], [5, 10], [15, 20], [21, 40]]
    def min_meeting_rooms(self, intervals) -> int:

        count = 1

        invl_prev = intervals[0][1]     # [0,30]

        for interval in intervals[1:]:      #[5,10]

            if invl_prev <= interval[0]:    #30 <= 5
                count +=1

            else:

                invl_prev = min(interval[1],invl_prev)      #

        return count


# Input = [[0, 30], [5, 10], [15, 20],[21,40]]
Input = [[7, 10], [2, 4]]
print(Solution().min_meeting_rooms(Input))
# Input = [[7, 10], [2, 4]]
