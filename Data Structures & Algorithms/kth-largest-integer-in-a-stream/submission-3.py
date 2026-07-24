class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        self.minHeap = nums
        self.k = k

        print(self.minHeap)


    def add(self, val: int) -> int:
        
        if self.k > len(self.minHeap):
            heapq.heappush(self.minHeap, val)
        elif val > self.minHeap[0]:
            heapq.heapreplace(self.minHeap, val)
        

        return self.minHeap[0]