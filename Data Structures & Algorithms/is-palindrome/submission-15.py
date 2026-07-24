class Solution:
    def isPalindrome(self, s: str) -> bool:

        l,r = 0, len(s) -1
        
        while l < r:
            if not self.isAlpha(s[l]):
                l+=1
                continue
            elif not self.isAlpha(s[r]):
                r-=1
                continue
            if s[l].lower() != s[r].lower():
                print(s[l], s[r])
                return False
            l+=1
            r-=1
            
        return True




    
    def isAlpha (self, c):
        return (ord('a') <= ord(c) <= ord('z') or 
        ord('A') <= ord(c) <= ord('Z') or
        ord('0') <= ord(c) <= ord('9'))
        