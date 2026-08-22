class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = [[] for i in range(len(nums) +1)]
        graph = {}
        res = []

        for n in nums:
            graph[n] = 1 + graph.get(n, 0)
        for n,c in graph.items():
            freq[c].append(n)

        for i in range(len(nums), -1, -1):
            for j in freq[i]:
                res.append(j)
                if k == len(res):
                    return res

        return res

