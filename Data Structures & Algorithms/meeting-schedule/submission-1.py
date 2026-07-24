"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key = lambda i:i.start)
        prevEnd = intervals[0].start

        for interval in intervals:
            if interval.start >= prevEnd:
                prevEnd = interval.end
            else:
                return False

        return True
