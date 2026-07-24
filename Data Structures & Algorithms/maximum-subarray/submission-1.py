class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSub= -1
        sub = -1
        
        for n in nums:
            sub = max(n, sub + n)
            maxSub = max(maxSub, sub)


        return maxSub