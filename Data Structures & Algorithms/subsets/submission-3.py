class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res, sol = [], []
        def back(i):
            if len(nums) == i:
                res.append(sol[:])
                return

            sol.append(nums[i])
            back(i+1)
            sol.pop()

            back(i+1)

        back(0)
        return res
        