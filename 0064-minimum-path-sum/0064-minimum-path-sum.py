class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        
        dp = [[0 for j in range(len(grid[0]) + 1)] for i in range(len(grid) + 1)]
         
        
        for i in range(len(dp)):
            
            dp[i][-1] = float('inf')
            
        for j in range(len(dp[0])):
            dp[-1][j] = float('inf')
            
        
        for i in range(len(grid) -1,-1,-1):
            for j in range(len(grid[i]) -1,-1,-1):
                
                if i == len(grid) -1 and j == len(grid[0]) -1:
                    dp[i][j] = grid[-1][-1]
                    continue
                
                dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + grid[i][j]
                
        
        print(dp)
        return dp[0][0]