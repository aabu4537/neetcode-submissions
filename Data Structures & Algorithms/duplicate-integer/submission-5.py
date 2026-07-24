class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # use set, iterate once through array and copmare to set

        sett = set()

        for num in nums:
            if num in sett:
                return True
            sett.add(num)
        
        return False
        