class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 1_000_000_007
        dp = [[0] * (n + 1) for i in range(n + 1)]
        
        for unpicked in range(n + 1):
            for undelivered in range(unpicked, n + 1):
                # If all orders are picked and delivered then,
                # for remaining '0' orders we have only one way.
                if not unpicked and not undelivered:
                    dp[unpicked][undelivered] = 1
                    continue
                
                # There are some unpicked elements left. 
                # We have choice to pick any one of those orders.
                if unpicked > 0:
                    dp[unpicked][undelivered] += unpicked * dp[unpicked - 1][undelivered]
                dp[unpicked][undelivered] %= MOD
                
                # Number of deliveries done is less than picked orders.
                # We have choice to deliver any one of (undelivered - unpicked) orders. 
                if undelivered > unpicked:
                    dp[unpicked][undelivered] += (undelivered - unpicked) * dp[unpicked][undelivered - 1]
                dp[unpicked][undelivered] %= MOD
            
        
        return dp[n][n]
        
        
        
        
        
        
        '''
        return factorial(n) % MOD
        @cache
        def dfs(p,d):
            
            if p == 0 and d == 0:
                return 1
            res = 0
            if p > 0:
                res += dfs(p-1, d) * p
                res %= MOD
            if p < d:
                res += dfs(p, d-1) * (d - p) 
                res %= MOD
            
            return res % MOD
        
        
        return dfs(n,n)
        
        '''
        
        
        
        
        