class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        cur = []

        def palindrome(c):
            return c == c[::-1]

        def helper(i):
            if i == len(s):
                res.append(cur[:])
                return
            if i > len(s):
                return
            for j in range(i, len(s)):
                sub = s[i:j+1]

                if palindrome(sub):
                    cur.append(sub)
                    helper(j+1)
                    cur.pop()


        helper(0)
        return res