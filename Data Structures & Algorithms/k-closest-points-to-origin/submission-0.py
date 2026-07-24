class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for x, y in points:
            distance = x*x + y*y
            heap.append([-distance, x, y])
        
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        res = []
        for d, x, y in heap:
            res.append([x, y])
        return res

        