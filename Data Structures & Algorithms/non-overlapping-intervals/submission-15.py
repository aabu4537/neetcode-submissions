class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        res = []
        intervals.sort(key= lambda i:i[0])
        count = 0

        for start, end in intervals:
            if not res or start >= res[-1][1]:
                res.append([start, end])
            else:
                res[-1][1] = min(res[-1][1], end)
                count+=1


        return count