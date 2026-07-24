class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res, sol = [], []

        nums.sort()

        def back(i):
            if i == len(nums):
                res.append(sol[:])
                return                
            sol.append(nums[i])
            back(i+1)
            sol.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            back(i+1)

        back(0)

        return res


        