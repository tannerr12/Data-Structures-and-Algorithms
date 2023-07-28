class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        def dfs(k,j):
            
            stack = []
            res = 0
            for i in range(k,j):
                
                if s[i] == '(':
                    stack.append(i)
                
                else:
                    idx = stack.pop()
                    if len(stack) == 0:
                        if i-idx-1 > 0:
                            res += 2 * dfs(idx+1,i)      
                        else:
                            res += 1
                        
                
            return res    
            
            
        return dfs(0,len(s))