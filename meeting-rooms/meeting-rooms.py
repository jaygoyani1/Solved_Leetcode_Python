class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1,len(intervals)):
            if (intervals[i-1][1] > intervals[i][0] or intervals[i-1][0] > intervals[i][1]):
                return False
        return True
        