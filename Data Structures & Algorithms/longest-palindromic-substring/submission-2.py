class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <2:
            return s
        max_res = ""

        for i in range(len(s) -1):
            res = ""
            l,r = i, i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                    l-=1
                    r+=1
            res += str(s[l+1:r])
            if len(res) > len(max_res): max_res = res

            res = ""
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                    l-=1
                    r+=1
            res += str(s[l +1:r])
            if len(res) > len(max_res): max_res = res

        return max_res