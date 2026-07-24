class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force mutiple each varaible and then divide by each number
        #want O(n) time complexity
        # [1,   1,  2, 8]
        # [48, 24,  6, 1]
        # [48, 24, 12, 8]

        res = [1] * len(nums)
        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        for j in range(len(nums) -1, -1, -1):
            res[j] *= suffix
            suffix *= nums[j]          


        return res
        