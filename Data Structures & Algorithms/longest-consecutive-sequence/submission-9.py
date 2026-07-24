class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        order = set(nums)
        max_count = 0

        for num in order:
            if num-1 not in order:
                count = 1
                cur = num
                while cur + 1 in order:
                    cur +=1
                    count+=1
                max_count = max(count, max_count)    

        
        return max_count