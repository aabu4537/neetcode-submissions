class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minHeap = []
        res = []

        for x, y in points[:k]:
            minHeap.append((-(x*x + y*y),x,y))

        heapq.heapify(minHeap)
        
        for x, y in points[k:]:
            distance = x*x + y*y
            if -distance > minHeap[0][0]:
                heapq.heapreplace(minHeap, (-distance, x, y))
        
        for d, x, y in minHeap:
            res.append((x,y))
        return res