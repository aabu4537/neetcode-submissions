class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        minHeap = []

        for n in nums[:k]:
            minHeap.append(n)
        
        heapq.heapify(minHeap)

        for n in nums[k:]:
            if n > minHeap[0]:
                heapq.heapreplace(minHeap, n)

        return minHeap[0] if nums else 0
        