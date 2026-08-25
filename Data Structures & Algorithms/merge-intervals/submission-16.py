class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #requirements / edgecases
        # <------------------->
        # --
        #     -------
        #          ----------    overlaps combine intervals. Empty lists?

        #arch - > loop through intervals array and compare end value to res 

        res = []
        intervals.sort()

        for start, end in intervals:
            if not res or start > res[-1][1]:
                res.append([start, end])
            else:
                res[-1][1] = max(res[-1][1], end)

        return res
