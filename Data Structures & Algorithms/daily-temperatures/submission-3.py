class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        size = len(temperatures)
        res= [0 for i in range(size)]
        
        for i in range(size):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                temp = stack.pop()
                res[temp] = i-temp
            stack.append(i)
        


        
        return res
        