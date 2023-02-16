class Solution:
    def twoEggDrop(self, n: int) -> int:
        #math problem... possible with top down
        
        dp = [[float('inf') for j in range(n+1)] for i in range(2+1)]
        
        
        dp[2][1] = 1
        dp[2][0] = 0
        for i in range(n+1):
            dp[1][i] = i
            
        
        
        for i in range(2,len(dp)):
            
            for j in range(1,n+1):
                
                for x in range(1,j):
                    
                    dp[i][j] = min(dp[i][j],1+ max(dp[i-1][x-1], dp[i][j-x]))
        
        
        
                    
            
        return dp[2][n]