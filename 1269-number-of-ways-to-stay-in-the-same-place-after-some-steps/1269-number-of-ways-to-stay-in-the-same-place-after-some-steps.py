class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        arrLen -= 1
        
        
        @cache
        def dfs(i, step):
            
            if step == steps:
                return i == 0
            
            res = 0
            
            if i < arrLen and steps - (step + 1) >= i+1:
                #step right
                res = (res + dfs(i+1, step + 1)) % MOD
            
            if i > 0:
                #step left
                res = (res + dfs(i-1, step + 1)) % MOD
            
            #stay
            if steps - (step + 1) >= i:
                res = (res + dfs(i, step + 1)) % MOD
            
            return res 
        
        
        return dfs(0,0)