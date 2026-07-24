class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        for n in nums[:k]:
            heap.append(n)
        
        heapq.heapify(heap)

        print(heap)
        for n in nums[k:]:
            if heap[0] < n:
                heapq.heapreplace(heap, n)
        
        return heap[0]