class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        
        
        def dfs(i,bitmap):
            
            if i > n:
                return 1
            
            res = 0
            for j in range(1,n + 1):
                
                if bitmap & (1 << j) > 0:
                    continue
                    
                elif gcd(j, i) == 1:
                    res += dfs(i+1, bitmap | (1 << j))
            
            
            return res
        
            
        return dfs(1, 0)
                    
                