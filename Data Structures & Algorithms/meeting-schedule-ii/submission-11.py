"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        rooms = []
        intervals.sort(key = lambda i:i.start)

        for meet in intervals:
            if not rooms or meet.start < rooms[0]:
                heapq.heappush(rooms, meet.end)
            else:
                heapq.heapreplace(rooms, meet.end)
            #rooms empty
            #cur interval falls within previous interval -> add room
            #cur interval starts after previous interval -> replace value in heap 
        return len(rooms)
        