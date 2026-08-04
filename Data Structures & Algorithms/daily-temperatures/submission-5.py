class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        res = [0 for i in range(len(temperatures))]
        print(res)
        
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                temp = stack.pop()
                res[temp] = i - temp
            stack.append(i)

        return res