class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()
        max_count = 0

        for n in nums:
            if n == n-1:
                continue
            cur = n
            count = 0
            while cur in nums:
                cur+=1
                count+=1
            max_count = max(max_count, count)
   
        
        return max_count