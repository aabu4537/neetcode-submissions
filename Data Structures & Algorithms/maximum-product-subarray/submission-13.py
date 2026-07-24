class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return nums[0]
        minP, maxP = 1,1
        final = 0

        for i in range(len(nums)):
            temp = max(nums[i], minP * nums[i], maxP * nums[i])
            minP = min(nums[i], minP * nums[i], maxP * nums[i])
            maxP = temp

            final = max(final, minP, maxP)

        return final