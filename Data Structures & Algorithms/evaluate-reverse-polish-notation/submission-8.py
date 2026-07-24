class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        res = 0

        for t in tokens:
            if t == "+":
                temp = int(stack.pop()) + int(stack.pop())
                stack.append(temp)
            elif t == "*":
                temp = int(stack.pop()) * int(stack.pop())
                stack.append(temp)
            elif t == "-":
                a, b = int(stack.pop()), int(stack.pop())
                temp = b-a
                stack.append(temp)
            elif t == "/":
                a, b = int(stack.pop()), int(stack.pop())
                temp= b/a
                stack.append(temp)    
            else:
                stack.append(t)
        
        return int(stack.pop())

        