class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        
        while len(nums)>k:
            heapq.heappop(nums)
        
        self.min_heap = nums
        self.k = k
        

    def add(self, val: int) -> int:
        if self.k > len(self.min_heap):
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)


        return self.min_heap[0]