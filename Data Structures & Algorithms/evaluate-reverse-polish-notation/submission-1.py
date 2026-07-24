class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        stack = []

        while i < len(tokens):
            
            if tokens[i] == '+':
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif tokens[i] == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif tokens[i] == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(tokens[i]))
            print(stack)
            i+=1
        

        return stack.pop()