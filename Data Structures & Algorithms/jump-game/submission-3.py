class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums)-1

        for i in range(goal-1, -1, -1):
            distance = i + nums[i]

            if distance >= goal:
                goal = i
            

        return goal == 0
            
        