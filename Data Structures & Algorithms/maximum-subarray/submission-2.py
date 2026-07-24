class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return nums[0]

        maxSub= -1
        sub = -1
        
        for n in nums:
            sub = max(n, sub + n)
            maxSub = max(maxSub, sub)

        return maxSub