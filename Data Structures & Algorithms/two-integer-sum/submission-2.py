class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # brute force loop through array to get first number loop again to get compliment / O(n^2) time probs

        #make hashmap to keep track of each number we have viewed so we dont have to loop again. we need to keep track of index too so im opting for hashmap or hashset
        #ensure time compleixty = O(n) space complexity O(n)
        #loop though and check if compliment is in hashset

        hashmap = {}

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in hashmap:
                return[hashmap[compliment], i]
            hashmap[num] = i
        
        return hashmap

        
        