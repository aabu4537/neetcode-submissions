class Solution:
    def jump(self, nums: List[int]) -> int:

        cur_end = jump = farthest = 0

        for i in range(len(nums)-1):
            farthest = max(nums[i]+i, farthest)
            if cur_end == i:
                jump+=1
                cur_end = farthest
        
        return jump






        