class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        res = 0
        stack = []
        great = 0 
        if x > y:
            great = 1
        else:
            great = 2
        for i in range(len(s)):
        
            stack.append(s[i])
                
            if great == 1 and len(stack) >=2 and stack[-1] == 'b' and stack[-2] == 'a':
                
                stack.pop()
                stack.pop()
                res += x
                
            elif great == 2 and len(stack) >= 2 and stack[-1] == 'a' and stack[-2] == 'b':
                stack.pop()
                stack.pop()
                res += y
        
        
        stack2 = []
        
        for c in stack:
            stack2.append(c)
            while len(stack2) >= 2 and ((stack2[-1] == 'a' and stack2[-2] == 'b') or (stack2[-1] == 'b' and stack2[-2] == 'a')):
                v1 = stack2.pop()
                v2 = stack2.pop()

                if v1 == 'b':
                    res += x
                elif v1 == 'a':
                    res += y

        
     

        return res
            
            
        
        