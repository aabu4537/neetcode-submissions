class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.append(newInterval)

        intervals.sort(key=lambda i:i[0])

        res = [intervals[0]]

        for start, end in intervals:
            if start > res[-1][1]:
                res.append([start, end])
            else:
                res[-1][1] = max(end, res[-1][1])

        return res
        