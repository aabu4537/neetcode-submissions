class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        dic = {}
        q = deque()
        max_heap = []
        for t in tasks:
            dic[t] = 1 + dic.get(t, 0)
        
        for c in dic.values():
            max_heap.append(-c)
        
        heapq.heapify(max_heap)
        time = 0
        while q or max_heap:
            time += 1
            if max_heap:
                top = heapq.heappop(max_heap)
                if top +1 != 0 :
                    q.append((top+1, time+n))

            if q:
                if q[0][1] <= time:
                    cnt, t = q.popleft()
                    heapq.heappush(max_heap, cnt)
        return time
                