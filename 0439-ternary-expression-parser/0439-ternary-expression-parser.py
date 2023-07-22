class Solution:
    def parseTernary(self, expression: str) -> str:
        
        
        
        def dfs(exr):
            res = None
            stack = []
            for i in range(1,len(exr)):
            
                if exr[i] == ':':
                    stack.pop()
                
                elif exr[i] == '?':
                    stack.append(i)
                
                if len(stack) == 0:
                    if exr[0] == 'T':
                        return dfs(exr[2:i])
                    else:
                        return dfs(exr[i+1:])
                    
            
            return exr
        
        return dfs(expression)
            