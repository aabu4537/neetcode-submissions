class Solution:
    def climbStairs(self, n: int) -> int:

        if n < 4:
            return n

        cur, prev = 1, 1

        for i in range(n -1):
            cur, prev = cur+prev, cur
        
        return cur
        