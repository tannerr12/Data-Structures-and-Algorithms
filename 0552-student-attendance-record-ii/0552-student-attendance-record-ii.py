class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        
        dp = [[[0,0,0] for j in range(2)] for i in range(n+1)]
        
        #6 states to start
        #print(dp)
        #No A, No L
        dp[1][0][0] = 1 #P
        dp[1][1][0] = 1 #A
        dp[1][0][1] = 1 #L
        
        #print(dp)
        
        
        for i in range(2, n+1):
            
            #No A No L ->    PP             PL               LL
            dp[i][0][0] = (dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2]) % MOD
            
            #A No L         PP             PL               LL        AL            ALL
            dp[i][1][0] = (dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2] + dp[i-1][1][0] + dp[i-1][1][1] + dp[i-1][1][2]) % MOD
            
            #No A 1 L
            dp[i][0][1] = dp[i-1][0][0] % MOD
        
            #No A 2 L
            dp[i][0][2] = dp[i-1][0][1] % MOD
            
            #A 1 L
            dp[i][1][1] = dp[i-1][1][0] % MOD
            
            #A 2 L
            dp[i][1][2] = dp[i-1][1][1] % MOD
            
    
    
        
        total = 0
        for j in range(2):
            for k in range(3):
                total += dp[n][j][k] % MOD
                total %= MOD
        
        
        return total
        