class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        max_count = 0

        for n in nums:
            if n-1 not in seen:
                count = 0 
                curr = n
                while curr in seen:
                    count+=1
                    curr +=1
                max_count = max(max_count, count)
                    
                
        return max_count


        