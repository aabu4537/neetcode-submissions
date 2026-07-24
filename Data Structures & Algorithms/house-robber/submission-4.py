class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 1:
            return 0
        
        prev, cur = 0,0

        for n in nums:
            prev, cur = cur, max(prev+n, cur)
            print(cur)
        
        return cur
        