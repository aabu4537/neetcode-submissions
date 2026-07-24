class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        heap = []
        freq = {}
        q = deque()
        for t in tasks:
            freq[t] = 1 + freq.get(t, 0)

        for l, f in freq.items():
            heap.append(-f)
        
        time = 0

        heapq.heapify(heap)
        while heap or q:
            time +=1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        
        return time

