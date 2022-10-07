class Solution:
    
    
    def integerBreak(self, n: int) -> int:
        originalN = n
        
        @lru_cache(maxsize=None)
        def dfs(remain, prod):
            nonlocal originalN
            
            if remain == 0:
                return prod
            
            
            m = 0
            for i in range(1,remain+1):
                if i == originalN:
                    continue
                m= max(m,dfs(remain - i, prod * i))
            
            
            return m
        
        
        return dfs(n,1)