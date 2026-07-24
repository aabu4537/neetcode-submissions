class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        max_count = 0

        for num in nums:
            if num -1 not in sett:
                curr = num
                counter = 0
                while curr in sett:
                    counter+=1
                    curr+=1
                max_count = max(max_count , counter)
        
        return max_count

        