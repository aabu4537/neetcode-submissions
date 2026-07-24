class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = []
        time = 0
        freq = {}

        for t in tasks:
            freq[t] = 1 + freq.get(t, 0)
        for t, f in freq.items():
            max_heap.append(-f)

        q = deque()
        heapq.heapify(max_heap)

        while q or max_heap:
            time +=1
            if max_heap:
                temp = 1 + heapq.heappop(max_heap)
                if temp:
                    q.append([temp, time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])


        return time
    