class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res, sol = [], []

        nums = sorted(candidates)
        def back(i, total):
            if total == target:
                res.append(sol[:])
                return
            if len(nums) == i or total > target:
                return
            
            sol.append(nums[i])
            back(i+1, nums[i]+total)
            sol.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            back(i+1, total)

        back(0, 0)
        return res