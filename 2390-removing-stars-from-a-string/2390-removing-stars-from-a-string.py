class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            
            if s[i] != '*':
                stack.append(s[i])
                
            else:
                stack.pop()
        
        
        return ''.join(stack)
            