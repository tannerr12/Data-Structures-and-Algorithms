class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        
        MOD = 10 ** 9 + 7
        
        @lru_cache(maxsize=1000)
        def dfs(n,k):
            
            if n == 0:
                return k <= 0

            res = 0
            #used bag
            res += dfs(n-1,k) * k
            res %= MOD
            if k > 0:
                #new bag
                res += dfs(n-1, k-1)
                res %= MOD
            
            return res % MOD
        
        
        return dfs(n,k) % MOD
        
    