class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res, sol = [], []
        n = len(nums)

        def back(i, total):
            if total == target:
                res.append(sol[:])
                return
            if n == i or total>target:
                return
            sol.append(nums[i])
            back(i, total+nums[i])
            sol.pop()
            back(i+1, total)

        back(0, 0)
        return res
            

        