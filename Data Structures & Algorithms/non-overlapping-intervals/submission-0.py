class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda i:i[0])

        count = 0
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] <= interval[0]:
                merged.append(interval)
            else:
                if merged[-1][1] > interval[1]:
                    merged[-1] = interval
                
                count+=1

        return count
            

    
        