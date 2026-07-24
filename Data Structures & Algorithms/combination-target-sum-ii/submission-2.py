class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res, sol = [], []

        candidates.sort()

        def back(i, total):
            if total == target:
                res.append(sol[:])
                return

            if i >= len(candidates) or total > target:
                return    
            
            sol.append(candidates[i])
            back(i+1, candidates[i] + total)
            sol.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            back(i+1, total)


        back(0, 0)
        return res