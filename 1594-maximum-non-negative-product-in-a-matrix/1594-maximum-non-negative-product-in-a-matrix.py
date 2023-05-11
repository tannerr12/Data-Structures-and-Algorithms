class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10 **9 + 7
        m,n = len(grid), len(grid[0])
        
        hasZero = False
        
        hasSign = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    hasZero = True
                
                if grid[i][j] < 0:
                    grid[i][j] = grid[i][j] * -1
                    hasSign[(i,j)] = -1
                else:
                    hasSign[(i,j)] = 1
                    
        @cache
        def dfs(i,j,s,t):
            
            if i == m -1 and j == n -1:
                s *= hasSign[(i,j)]
                if s == 1:
                    return t * grid[i][j]
                
                else:
                    return -1
            
            res = -1
            
            if i+1 != m:
                res = max(res, dfs(i+1,j,s*hasSign[(i,j)], t * grid[i][j]))
            if j+1 != n:
                res = max(res,dfs(i,j+1,s*hasSign[(i,j)], t * grid[i][j]))
            
            
            return res
        
        
        val = dfs(0,0,1,1)
        if val <= 0:
            if hasZero:
                return 0
            else:
                return -1
        return val % MOD