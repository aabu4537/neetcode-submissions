class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []

        pairs = sorted(zip(position, speed), reverse=True)

        for p, s in pairs:
            time = (target - p)/s
            if stack and stack[-1] >= time:
                continue            
            stack.append(time)

        return len(stack)