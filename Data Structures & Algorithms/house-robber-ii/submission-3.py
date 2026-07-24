class Solution:
    def rob(self, nums: List[int]) -> int:

        return max(nums[0], self.Helper(nums[1:]), self.Helper(nums[:-1]))

    def Helper(self, nums):
        prev, cur = 0,0
        for n in nums:
            prev, cur = cur, max(prev+n, cur)
        return cur
