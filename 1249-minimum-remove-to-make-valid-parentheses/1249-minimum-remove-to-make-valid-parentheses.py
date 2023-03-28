class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        
        res = []
        stack = []
        invalid = set()
        for i in range(len(s)):
            
        #   if s[i] != '(' and s[i] != ')':
        #       res.append(s[i])
            
            if s[i] == '(':
                stack.append(['(', i])
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    invalid.add(i)
        
        while stack:
            v, idx = stack.pop()
            invalid.add(idx)
            
        
        #print(invalid)
         
        for i in range(len(s)):
            
            if i in invalid:
                continue
            
            res.append(s[i])
            
        
        
        return ''.join(res)
                
        