class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = [[] for i in range(len(nums) +1)]
        res = []
        count = {}

        for n in nums:
            count[n] = count.get(n,0) +1
        for n, c in count.items():
            freq[c].append(n)

        
        for i in range(len(freq)-1, -1,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
            
        