class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        def dfs(s):
            
            stack = []
            res = 0
            for i in range(len(s)):
                
                if s[i] == '(':
                    stack.append(i)
                
                else:
                    idx = stack.pop()
                    if len(stack) == 0:
                        if len(s[idx+1:i]) > 0:
                            res += 2 * dfs(s[idx+1:i])      
                        else:
                            res += 1
                        
                
            return res    
            
            
        return dfs(s)