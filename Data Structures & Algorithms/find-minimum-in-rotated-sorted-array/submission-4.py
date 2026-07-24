class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) -1

        while l < r:
            m = (r+l)//2        
            if nums[r] < nums[m]:
                l = 1+m
            else:
                r = m
            print(nums[l])
        
        return nums[l]
        