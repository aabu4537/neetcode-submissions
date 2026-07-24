class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:

        r = 0
        res = []

        while r < len(s):
            l = r
            while s[r] != "#":
                r+=1
            count = int(s[l:r])
            res.append(s[r+1: r+count+1])
            r = r+count+1

        return res