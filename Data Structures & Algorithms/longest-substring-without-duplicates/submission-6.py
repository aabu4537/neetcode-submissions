class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        max_count = 0
        l, r = 0, 0

        while r < len(s):
            if s[r] in sett:
                while s[r] in sett:
                    sett.remove(s[l])
                    l+=1
            sett.add(s[r])
            r+=1
            max_count = max(r-l, max_count)
            print(sett)

        return max_count
        