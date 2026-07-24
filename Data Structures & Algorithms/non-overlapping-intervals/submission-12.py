class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        count = 0
        intervals.sort()
        last_end = intervals[0][1]

        for start, end in intervals[1:]:
            if last_end <= start:
                last_end = end
            else:
                last_end = min(end, last_end)
                count+=1
                
        return count
        