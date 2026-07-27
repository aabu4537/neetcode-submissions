class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res +=  str(len(s))+ "#" + s
        return res


    def decode(self, s: str) -> List[str]:

        l, r = 0, 0
        res = []
#  5#Hello
        while r < len(s):
            while s[r] != "#":
                r+=1
            number = int(s[l:r])
            res.append(s[r+1:r+number+1])
            r = r + number +1
            l = r
            
    
        return res
