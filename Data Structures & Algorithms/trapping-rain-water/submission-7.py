class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxl, maxr = 0,0
        n = len(height)
        l, r = [0] * n , [0] * n
        res = 0

        for i in range(n):
            j = n - 1 - i
            l[i] = maxl
            r[j] = maxr
            maxl = max(height[i] , maxl)
            maxr = max(height[j], maxr)

        for i in range(n):
            res += max(0, min(l[i], r[i]) - height[i])
        
        return res