class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def Helper(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            cur.append(nums[i])    
            Helper(i, cur, nums[i]+total)
            cur.remove(nums[i])
            Helper(i+1, cur, total)



        Helper(0, [], 0)
        return res    