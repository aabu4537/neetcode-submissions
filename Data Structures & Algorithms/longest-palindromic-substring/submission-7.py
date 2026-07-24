class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) < 2:
            return s
        
        max_res = ""
        
        def helper(l, r):
            while l >=0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return str(s[l+1:r])
            
           
        for i in range(len(s)):
            max_res = max(max_res, helper(i,i), helper(i, i+1), key=len)
        
        
        return max_res
        