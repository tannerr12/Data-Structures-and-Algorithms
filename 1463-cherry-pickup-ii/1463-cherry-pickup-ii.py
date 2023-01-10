class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        
        #dp = [[0,-1] for j in range(len(grid[0]) +2)] for i in range(len(grid) +1)]
        
        #dp[1][1] = [0,1]
        #dp[1][-2] = [0, 2]
        #for i in range(len(grid)-1,-1,-1):
            
        #    for j in range(len(grid[0])-1,-1,-1):
                
        #        if dp:
        #        dp[i][j+1] = max(dp[i+1][j+1], dp[i+1][j], dp[i][j+2]) + grid[i][j]
                
        
        
        #print(dp)
        @cache
        def dfs(i,j,k):
            
            if i == len(grid):
                return 0
            
            
            res = grid[i][j] if j == k else grid[i][j] + grid[i][k]
            
            r = 0
            for c1 in range(-1,2):
                
                for c2 in range(-1,2):
                    
                    if j + c1 >=0 and j + c1 < len(grid[0]) and k + c2 >= 0 and k + c2 < len(grid[0]):
                        r = max(r,dfs(i + 1, j+c1, k + c2))
            
            return res + r
        
        
        return dfs(0,0, len(grid[0]) -1)