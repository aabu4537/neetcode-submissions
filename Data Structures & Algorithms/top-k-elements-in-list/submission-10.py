class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = [[] for i in range(len(nums) +1)]
        res = []
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for c, n in count.items():
            freq[n].append(c)

        for i in range(len(freq) -1, -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res        