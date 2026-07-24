class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l,r = 0,0
        max_count = 0
        seen = set()

        while r < len(s):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1   
            max_count = max(max_count, (r-l) + 1)
            seen.add(s[r])
            r+=1
            
        
        return max_count
        