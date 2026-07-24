class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        hashmap = {}
        
        for i, num in enumerate(numbers):
            compliment = target - num
            if compliment in hashmap:
                return [hashmap[compliment]+1, i+1]
            hashmap[num] = i
        
            
        