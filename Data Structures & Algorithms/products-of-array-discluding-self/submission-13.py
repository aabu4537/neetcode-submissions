class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = suffix = 1
        size = len(nums)
        res = [1 for i in range(size)]
        for i in range(size):
            res[i] *= prefix
            prefix *= nums[i]
        for i in range(size-1, -1, -1):
            res[i] *=suffix
            suffix *= nums[i]
        return res
        