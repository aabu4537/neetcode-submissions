class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return max(nums)

        def Helper(n):
            prev, cur = 0,0
            if n ==0 :
                for i in range(1, len(nums)):
                    temp = max(nums[i]+prev, cur)
                    prev = cur
                    cur = temp
            elif n ==1:
                for i in range(len(nums) - 1):
                    temp = max(nums[i]+prev, cur)
                    prev = cur
                    cur = temp
            return cur

        
        
        return max(Helper(0), Helper(1))