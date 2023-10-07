class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        
        MOD = 10 ** 9 + 7
        
        @cache
        def dfs(cur, rem, size):
            
            if rem < 0:
                return 0
            
            if size == 0:
                return rem == 0
            
            
            res = (dfs(cur, rem, size - 1) * cur) % MOD
            
            for i in range(cur+1, m+1):
                res = (res + dfs(i, rem - 1, size - 1)) % MOD
                
            
            return res 
        
        
        return dfs(0, k, n)