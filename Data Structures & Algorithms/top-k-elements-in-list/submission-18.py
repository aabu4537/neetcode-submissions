class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = [[] for i in range(len(nums) +1)]
        graph = {}
        res = []
        for n in nums:
            graph[n] = 1+ graph.get(n, 0)
        for n, p in graph.items():
            freq[p].append(n)

        for i in range(len(freq)-1, -1,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res

        