class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res, sol = [], []

        def back():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for n in nums:
                if n not in sol:
                    sol.append(n)
                    back()
                    sol.pop()
        
        back()
        return res