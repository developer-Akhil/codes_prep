#Type: Easy
# Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei),determine
# if a person could attend all meetings.

# videos : https://www.youtube.com/watch?v=PaJxqZVPhbg
# website: zhenyu0519.github.io/2020/07/13/lc253/

# Input:    [[0,30],[5,10],[15,20]]
# Output:   false

# Input:    [[7,10],[2,4]]
# Output:   true


class Solution:

    def canAttendMeetings(self,intervals):

        intervals.sort(key = lambda i:i[0])         # [[0,30],[5,10],[15,20]]

        # sorted(intervals, key=lambda x: x[0])

        for i in range(1,len(intervals)):

            i1 = intervals[i-1]                 # [0,30]
            i2 = intervals[i]                   # [5,10]

            if i1[1] > i2[0]:                   # if i1[1] > i2[0] if 30 > 5
                return False
        return True

intervals = [[9,11],[11,1],[12,2]]
# intervals=[[0,30],[5,10],[15,20]]
print(Solution().canAttendMeetings(intervals))
