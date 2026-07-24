class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        l, best = 0 , 0 


        for r in range(len(s)):
            if s[r] in seen:
                while s[r]  in seen:
                    seen.remove(s[l])
                    l+=1
            best = max(best, r - l +1)
            seen.add(s[r])

        return best