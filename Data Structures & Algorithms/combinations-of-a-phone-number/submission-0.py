class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        letter = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        res = []
        cur = []
        def helper(i):
            if i == len(digits):
                res.append("".join(cur))
                return
            
            num = int(digits[i])
            
            for l in letter[num]:
                cur.append(l)
                helper(i+1)
                cur.pop()
        helper(0)
        return res
