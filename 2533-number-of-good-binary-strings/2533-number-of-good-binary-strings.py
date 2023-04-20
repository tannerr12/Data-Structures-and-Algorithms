class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
                

        MOD = 10**9 + 7
        
        
        @cache
        def dfs(i,x):
    
            if i > maxLength:
                return 0
            
            res = 0
            if i >= minLength and i <= maxLength:
                res = 1
                
            res += dfs(i + zeroGroup,0) % MOD
            
            res += dfs(i + oneGroup,1) % MOD
            
            return res % MOD
    
        return dfs(0,0)
        
     