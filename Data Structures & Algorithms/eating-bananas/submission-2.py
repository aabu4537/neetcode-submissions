class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l,r = 1, max(piles)

        def helper(r):

            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p/r)
            return total_hours


        while l < r:
            m = l+ (r-l)//2
            hours = helper(m)

            if hours > h:
                l = m+1
            else:
                r = m
    
        return l
        