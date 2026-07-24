class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        final = nums[0]
        min_p, max_p = 1,1

        for i in range(len(nums)):            
            curr_min = min(nums[i] * min_p, nums[i] * max_p, nums[i])            
            curr_max = max(nums[i] * min_p, nums[i] * max_p, nums[i])            
            
            min_p, max_p = curr_min, curr_max
            final = max(max_p, final)
        return final

        