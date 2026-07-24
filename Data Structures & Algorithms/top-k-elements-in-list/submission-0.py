class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #hashmap holds {count: frequency} 
        # [1, 2, 3, 4, 5. 6]
        # [1, 2, 3, 0, 0, 0]
        # order it and return an array of the top k
        #frequency for how many words in the list
        #result array

        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        result = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, c in count.items():
            freq[c].append(num)
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result



        