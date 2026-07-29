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
        heapq.heapify(rooms)
        intervals.sort(key = lambda i:i.start)

        for meet in intervals:
            if not rooms:
                heapq.heappush(rooms, meet.end)
            elif meet.start >= rooms[0]:
                heapq.heapreplace(rooms, meet.end)
            else:
                heapq.heappush(rooms, meet.end)
            
        return len(rooms)
        