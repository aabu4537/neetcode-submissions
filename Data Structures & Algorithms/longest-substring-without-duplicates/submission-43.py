class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 2:
            return len(s)

        max_sub = 0
        seen = set()
        l = 0
        for r in range(len(s)):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
            max_sub = max(max_sub, (r-l+1) ) 
            seen.add(s[r])
        
        return max_sub