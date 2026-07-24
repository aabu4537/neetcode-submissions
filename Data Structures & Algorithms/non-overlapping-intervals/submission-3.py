class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda i:i[0])
        count = 0
        prev = intervals[0][1]

        for interval in intervals[1:]:
            if prev <= interval[0]:
                prev = interval[1]
            else:
                prev = min(prev, interval[1])
                count +=1
        return count                
            

    
        