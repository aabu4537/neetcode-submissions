class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_counter = 0
        sett = set(nums)

        for num in nums:
            if num-1 not in sett:
                length = 0
                while num + length in sett:
                    length += 1
                max_counter = max(length, max_counter)
        
        return max_counter
                

            
        
        