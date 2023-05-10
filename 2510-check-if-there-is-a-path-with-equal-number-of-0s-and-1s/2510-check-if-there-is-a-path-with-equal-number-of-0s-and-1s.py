class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        m,n = len(grid)-1, len(grid[0])-1
        for i in range(m +1):
            for j in range(n +1):
                
                if grid[i][j] == 0:
                    grid[i][j] = -1
        
        @cache
        def dfs(i,j,k):
            if i > m or j > n:
                return False
            if i == m and j == n:
                return k + grid[i][j] == 0
            
            
            res = False
            
            res = dfs(i+1,j,k + grid[i][j]) or dfs(i,j+1,k + grid[i][j])
            
            
            return res
        
        
        return dfs(0,0,0)