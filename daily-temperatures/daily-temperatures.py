class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
  
            while stack and temperatures[i] > stack[len(stack) -1][0]:
                    temp, pos = stack.pop()
                    res[pos] = i - pos

            
            
            stack.append((temperatures[i], i))
        
        
        return res