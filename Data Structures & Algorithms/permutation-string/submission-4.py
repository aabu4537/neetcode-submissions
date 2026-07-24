class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            
        if len(s1) > len(s2):
            return False
        alphabet1 = [0] * 26
        alphabet2 = [0] * 26

        for i in range(len(s1)):
            alphabet1[ord(s1[i]) - ord('a')] +=1

        for i in range(len(s1)):
            alphabet2[ord(s2[i]) - ord('a')] +=1
        
        if alphabet1 == alphabet2:
            return True
        
        for i in range(len(s1), len(s2)):
            alphabet2[ord(s2[i]) - ord('a')] +=1
            alphabet2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if alphabet1 == alphabet2:
                return True
        
        return False
            
