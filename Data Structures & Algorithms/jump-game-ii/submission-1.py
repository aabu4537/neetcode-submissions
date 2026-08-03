class Solution:
    def jump(self, nums: List[int]) -> int:
        
        cur_end = 0
        farthest = 0
        jumps = 0

        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i])
            if cur_end == i:
                jumps+=1
                cur_end = farthest
        return jumps