class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m,n = len(grid), len(grid[0])
        
        def checkPar(st):
            
            stack = []
            
            for p in st:
                if p == ')' and not stack:
                    return False
                if p == ')' and stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(p)
            return len(stack) == 0
                
        
        @cache
        def dfs(r,c,s):
            
            if r >= m or c >= n:
                return False
            
            
            p = grid[r][c]
            if p == ')' and len(s) == 0:
                return False
            if p == ')' and len(s) > 0 and s[-1] == '(':
                s = s[:-1]
            
            else:
                s += p
                
            
            
            if r == m-1 and c == n-1:
                
                return len(s) == 0
            

            res = False    
            #go right
            res = res or dfs(r+1,c,s)
            #go down
            res = res or dfs(r,c+1,s)
            
            return res
        
        return dfs(0,0,'')
    
            
            
                