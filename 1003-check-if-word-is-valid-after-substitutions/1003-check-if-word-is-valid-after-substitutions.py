class Solution:
    def isValid(self, s: str) -> bool:
        
        c = Counter(s)
        
        if s[0] != 'a' or c['a'] != c['b'] or c['a'] != c['c'] or 'abc' not in s:
            return False
        
        
        stack = []
        
        
        for i in range(len(s)):
            
            char = s[i]
            if char != 'c':
                stack.append(char)
                
            if char == 'c':
                if not stack or stack[-1] != 'b':
                    return False
                stack.pop()
                if not stack or stack[-1] != 'a':
                    return False
                stack.pop()
        
        return len(stack) == 0
            
            