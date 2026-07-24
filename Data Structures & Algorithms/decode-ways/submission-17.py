class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        prev, cur = 1,1

        for i in range(1, len(s)):
            val = 0

            if s[i] != "0":
                val += cur
            
            if 10 <= int(s[i-1: i+1]) <= 26:
                val += prev
            
            prev, cur = cur, val
        
        return cur