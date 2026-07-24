class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {} # {key: occurances, values: acutal num from list}
        freq = [[] for i in range(len(nums) +1)]
        print(freq)
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            print(n,c)
            freq[c].append(n)

        for i in range(len(freq)-1, -1, -1):
            for j in freq[i]:
                res.append(j)
                if k == len(res):
                    return res