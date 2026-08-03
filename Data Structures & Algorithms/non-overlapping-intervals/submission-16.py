class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        
        intervals.sort(key= lambda i:i[0])
        prev_end = intervals[0][1]
        count = 0

        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                prev_end = min(prev_end, end)
                count+=1


        return count-1