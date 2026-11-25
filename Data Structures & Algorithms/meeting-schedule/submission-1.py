"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        """
        If two intervals are sorted in ascending order by their start values, 
        they overlap if 
        the start value of the second interval 
        is less than the end value of the first interval. 
        """
        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]
            
            if i2.start < i1.end:
                return False
        return True