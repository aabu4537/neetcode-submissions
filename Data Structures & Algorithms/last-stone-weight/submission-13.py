class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-s for s in stones]

        heapq.heapify(stones)
        i, res = 0,0
        while len(stones)> 1:
            one, two = heapq.heappop(stones) ,heapq.heappop(stones)
            if one != two:
                heapq.heappush(stones, (one - two))
        return -stones[0] if stones else 0
