class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1,1

        for n in nums:

            curMin, curMax  = min(curMax * n, n * curMin, n) , max(n * curMax, n * curMin, n) 
            res = max(res, curMax, curMin)

        return res
        
        