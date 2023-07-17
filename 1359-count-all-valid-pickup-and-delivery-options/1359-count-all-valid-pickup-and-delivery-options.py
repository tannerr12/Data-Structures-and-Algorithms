class Solution:
    def countOrders(self, n: int) -> int:
        
        MOD = 10 ** 9 + 7
        
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
        
        

        
        
        