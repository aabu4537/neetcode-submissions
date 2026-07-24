class Solution:
    def rob(self, nums: List[int]) -> int:

        return max(self.Helper(nums[1:]), self.Helper(nums[:-1]), nums[0])

    
    def Helper(self, nums):
        
        prev, cur = 0,0

        for n in nums:
            prev, cur = cur, max(cur, prev+n)
        return cur
        