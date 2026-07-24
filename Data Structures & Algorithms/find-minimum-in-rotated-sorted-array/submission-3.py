class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1

        while l < r:
            m = (l+r) //2
            print(l)
            if nums[r] < nums[m]:
                l = 1+m
            else:
                r = m
        
        return nums[l]
                
        