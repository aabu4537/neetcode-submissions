class Solution:
    def rob(self, nums: List[int]) -> int:

        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        
    
    def helper(self, nums):

        if len(nums) < 1:
            return 0

        prev, cur = 0,0
        for n in nums:
            prev, cur = cur, max(cur, prev+n)
        return cur
        