class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        dp = {}
        
        
        for r in range(row -1,-1,-1):
            
            for c in range(col-1,-1,-1):
                if obstacleGrid[r][c] == 1:
                    dp[(r,c)] = 0
                elif r == row -1 and c == col -1:
                    
                    dp[(r,c)] = 1
                
                elif r +1 >= row:
                    
                    dp[(r,c)] = dp[(r,c+1)]
                elif c +1 >= col:
                    dp[(r,c)] = dp[(r+1,c)]
                
                
                else:
                    
                    dp[(r,c)] = dp[(r+1,c)] + dp[(r,c+1)]
                    
        
        
        #print(dp)
        return dp[(0,0)]