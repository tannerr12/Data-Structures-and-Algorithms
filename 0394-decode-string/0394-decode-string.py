class Solution:
    def decodeString(self, s: str) -> str:
        
        
        
        stack = []
        
        
        for i in range(len(s)):
            
            char = s[i]
            
            
            if char != ']':
            
                stack.append(char)
            else:
                
                
                temp = ''
                
                while stack and stack[-1] != '[':
                    temp = stack.pop() + temp
                    
                
                stack.pop()
                
                k = ''
                
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                
                
                
                stack.append(int(k) * temp)
                
        
        
        
        return ''.join(stack)