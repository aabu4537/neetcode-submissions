class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)
        max_count = 0

        for n in nums:
            if n-1 not in seen:
                cur = n
                count = 0
                while cur in seen:
                    cur+=1
                    count+=1
                max_count = max(max_count, count)

        return max_count

        