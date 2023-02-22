class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * numPeople  
        dp[0] = 1
        
        for i in range(1,numPeople):
            dp[i] = dp[i-1] * 2 * (2*i+1)//(i+2) 
        
        
       # print(dp)
        
        return dp[(numPeople//2) -1] % MOD