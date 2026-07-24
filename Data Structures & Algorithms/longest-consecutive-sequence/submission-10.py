class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        order = set(nums)
        max_count = 0

        for num in order:
            if num-1 not in order:
                cur = num
                count = 0
                while cur in order:
                    cur +=1
                    count +=1
                max_count = max(max_count, count)

        return max_count
        