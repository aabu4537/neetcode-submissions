class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)
        max_count = 0

        for n in seen:
            if n-1 not in seen:
                curr = n
                counter = 0
                while curr in seen:
                    curr +=1
                    counter +=1
                max_count = max(max_count, counter)
        return max_count
        