class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        
        if d > len(jobDifficulty):
            return -1
        
        
        dp = [[float('inf') for i in range(d +1)] for j in range(len(jobDifficulty))]
       
        dp[-1][d] = jobDifficulty[-1]
    
        for i in range(len(jobDifficulty) -2,-1,-1):
            
            
            dp[i][d] = max(dp[i+1][d], jobDifficulty[i])
        
        print(dp)
        
        for dd in range(d-1, 0,-1):
            
            for i in range(dd-1, len(jobDifficulty) - (d - dd)):
                
                hardest = 0
                for j in range(i, len(jobDifficulty) - (d - dd)):
                    hardest = max(jobDifficulty[j], hardest)
                    dp[i][dd] = min(dp[i][dd], hardest + dp[j+1][dd+1])
                
        
        
        return dp[0][1]
                    
                
                
            
        