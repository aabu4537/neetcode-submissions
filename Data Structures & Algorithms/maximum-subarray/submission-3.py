class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSub= nums[0]
        sub = 0
        
        for n in nums:
            sub = max(n, sub + n)
            maxSub = max(maxSub, sub)

        return maxSub