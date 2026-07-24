class Solution:
    def trap(self, height: List[int]) -> int:

        maxl = 0
        maxr = 0
        l = [0] * len(height)
        r = [0] * len(height)
        res = 0
        n = len(height)

        for i in range(n):
            j = n-1-i
            l[i] = maxl
            r[j] = maxr
            maxl = max(height[i], maxl)
            maxr = max(height[j], maxr)
        
        for i in range(n):
            res += max(0, min(r[i], l[i]) - height[i])
        return res
        