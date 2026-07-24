class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for x, y in points[:k]:
            distance = math.sqrt(x*x + y*y)
            heap.append([-distance, x, y])
        
        heapq.heapify(heap)

        for x, y in points[k:]:
            distance = -(math.sqrt(x*x + y*y))
            if heap[0][0] < distance:
                heapq.heapreplace(heap, [distance, x, y])

        res = []
        for d, x, y in heap:
            res.append([x, y])
        return res

        