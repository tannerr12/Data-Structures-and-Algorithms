class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        
        mod = 10 ** 9 +7
        
        dp = [[[0]*k for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                
                if i ==0 and j == 0:
                    dp[i][j][grid[i][j] % k ] += 1
                
                
                elif i == 0:
                    for key in range(k):
                        dp[i][j][(key + grid[i][j]) % k]  += dp[i][j-1][key] % mod
                elif j == 0:
                    for key in range(k):
                        dp[i][j][(key + grid[i][j]) % k]  += dp[i-1][j][key] % mod
                        
                else:
                    for key in range(k):
                        dp[i][j][(key + grid[i][j]) % k]  += dp[i][j-1][key] % mod
                        dp[i][j][(key + grid[i][j]) % k]  += dp[i-1][j][key] % mod
        
        
        return dp[m-1][n-1][0] % mod
        