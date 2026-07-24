class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        longest = ""

        def center (l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]

        for i in range(len(s) -1):
            longest = max(longest, center(i,i), center(i,i+1), key=len)
        
        return longest
        