class Solution:
    def trap(self, height: List[int]) -> int:

        maxl = 0
        maxr = 0
        l = [0] * len(height)
        r = [0] * len(height)
        res = 0

        for i in range(len(height)):
            l[i] = maxl
            maxl = max(height[i], maxl)
        
        for i in range(len(height)-1, -1,-1):
            r[i] = maxr
            maxr = max(height[i], maxr)
        
        for i in range(len(height)):
            if min(r[i], l[i]) - height[i] >0:
                res += min(r[i], l[i]) - height[i]
        return res
        