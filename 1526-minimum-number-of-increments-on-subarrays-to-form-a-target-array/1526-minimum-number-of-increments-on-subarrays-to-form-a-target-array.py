class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        res = 0
        stack = []
        dp = [0] * len(target)
        sub = 0
        for i in range(len(target)):
            v = target[i] - sub
            if v < 0:
                res += (v * -1) 
                sub -= (v * -1)
                
            
            if stack and v > stack[-1]:
                sub += stack[-1]
                if len(stack) > 1:
                    res += stack[0] - stack[-1]
                
                stack = []
            
            
            stack.append(target[i] - sub)
        
        
        if stack:
            res += stack[0]
        return res + sub