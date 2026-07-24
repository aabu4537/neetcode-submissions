class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        freq = [[] for i in range(len(nums) + 1)]
        result = []

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        for i, j in hashmap.items():
            freq[j].append(i)

        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result            
            