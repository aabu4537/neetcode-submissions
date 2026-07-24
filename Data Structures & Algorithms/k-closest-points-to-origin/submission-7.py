class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        maxHeap = []
        res = []

        for x, y in points[:k]:
            maxHeap.append((-(x*x + y*y),x,y))

        heapq.heapify(maxHeap)
        
        for x, y in points[k:]:
            distance = x*x + y*y
            if -distance > maxHeap[0][0]:
                heapq.heapreplace(maxHeap, (-distance, x, y))
        
        for d, x, y in maxHeap:
            res.append((x,y))
        return res