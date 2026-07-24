class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <2:
            return s

        max_res = ""

        def center(l, r):
            while l >= 0 and r < len(s) and s[r] == s[l]:
                l-=1
                r+=1
            return s[l+1:r]

        for i in range(len(s) -1):
            max_res = max(max_res, center(i, i), center(i, i+1), key=len)

        return max_res