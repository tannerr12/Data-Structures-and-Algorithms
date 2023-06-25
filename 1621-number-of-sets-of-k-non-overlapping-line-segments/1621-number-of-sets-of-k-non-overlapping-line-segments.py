class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        
        @lru_cache(maxsize=100000)
        def dfs(i,k,place):
            
            if k == 0:
                return 1
            if i >= n:
                return 0
            res = 0
            
            #skip
            res += dfs(i+1,k,place)
            res %= MOD
            
            if not place:
                #placed here
                res += dfs(i+1,k,True)
                res %= MOD
            else:
                #place the end point
                res += dfs(i,k-1,False)
                res %= MOD
                
            
            return res % MOD
        
        
        return dfs(0,k,False) % MOD
                
            