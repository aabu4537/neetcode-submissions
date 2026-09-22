class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        pairs = {
            ')':'(',
            '}':'{',
            ']':"["
        }
        
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if len(stack) == 0 or pairs[c] != stack.pop():
                    return False
        
        return len(stack) ==0