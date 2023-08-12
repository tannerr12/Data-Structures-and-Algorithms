class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if obstacleGrid[-1][-1] == 1:
            return 0
        
        dp = [[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        
        dp[-1][-1] = 1
        for i in range(len(obstacleGrid[0]) -2,-1,-1):
            
            if obstacleGrid[-1][i] != 1:
                dp[-1][i] = dp[-1][i+1]
            
        for j in range(len(obstacleGrid) -2,-1,-1):
            if obstacleGrid[j][-1] != 1:
                dp[j][-1] = dp[j+1][-1]
            
        
        for i in range(len(obstacleGrid) -2, -1,-1):
            for j in range(len(obstacleGrid[0]) -2,-1,-1):
                
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
        return dp[0][0]