class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        alphabet = [0] * 26

        for c in range(len(s)):
            alphabet[ord(s[c]) - ord('a')] += 1
            alphabet[ord(t[c]) - ord('a')] -= 1
        
        for i in range(len(alphabet)):
            print(alphabet[i])
            if alphabet[i] != 0:
                return False
        
        return True
        
        
        