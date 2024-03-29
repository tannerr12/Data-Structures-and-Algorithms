class Solution:
    def tribonacci(self, n: int) -> int:
        """
        if n <= 1:
            return n
        if n == 2:
            return 1
        dp = [0] * (n +1)
        
        dp[0] = 0
        dp[1] = 1 
        dp[2] = 1
        
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
        
        return dp[n]
        """
    
    
        
        @cache
        def trib(n):
            
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            
            
            return trib(n-1) + trib(n-2) + trib(n-3)
        
        
        return trib(n)
        