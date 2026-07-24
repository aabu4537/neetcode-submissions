class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) < 2:
            return s
        
        max_res = ""
        for i in range(len(s)):
            res = ""
            l,r = i,i
            while l >=0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            res += str(s[l+1:r])
            max_res = max(res, max_res, key=len)

            res = ""
            l,r = i,i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            res += str(s[l+1:r])
            max_res = max(res, max_res, key=len)


        
        return max_res
        