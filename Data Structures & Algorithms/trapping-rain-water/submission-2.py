class Solution:
    def trap(self, height: List[int]) -> int:

        maxl = 0
        maxr = 0
        l = [0] * len(height)
        r = [0] * len(height)
        res = 0

        for i in range(len(height)):
            j = -i-1
            l[i] = maxl
            r[j] = maxr
            maxl = max(height[i], maxl)
            maxr = max(height[j], maxr)
        
        for i in range(len(height)):
            res += max(0, min(r[i], l[i]) - height[i])
        return res
        