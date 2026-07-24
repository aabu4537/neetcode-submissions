class Solution:
    def countSubstrings(self, s: str) -> int:

        if len(s)<1:
            return 0

        count = 0

        def helper(l,r):
            temp = 0
            while l >=0 and r < len(s) and s[r] == s[l]:
                    l-=1
                    r+=1
                    temp+=1
            return temp

        for i in range(len(s)):
            count += helper(i, i) + helper(i, i+1)
            

        return count    