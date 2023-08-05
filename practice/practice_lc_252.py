# Input:    [[0,30],[5,10],[15,20]]
# Output:   false

class Solution:

    def canAttendMeetings(self, intervals):

        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):

            if intervals[i - 1][1] > intervals[i][0]:
                return False

        return True

intervals = [[9,11],[11,1],[12,2]]

# intervals = [[0, 4], [5, 10], [15, 20]]
print(Solution().canAttendMeetings(intervals))
