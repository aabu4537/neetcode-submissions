class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return nums[0]

        prev, cur = 0, 0 

        for i in range(0, len(nums)-1):
            prev, cur = cur, max(cur, prev+nums[i])
        
        prev1, cur1 = 0, 0 

        for i in range(1, len(nums)):
            prev1, cur1 = cur1, max(cur1, prev1+nums[i])



        return max(cur, cur1)
        