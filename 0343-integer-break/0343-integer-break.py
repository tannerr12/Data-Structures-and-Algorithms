class Solution:
    
    
    def integerBreak(self, n: int) -> int:
        originalN = n
        
        memo = {}
        @lru_cache(maxsize=None)
        def dfs(remain, prod):
            nonlocal originalN
            
            if remain == 0:
                return prod
            
            
            if (remain) in memo:
                return memo[(remain)]
            
            m = 0
            for i in range(1,remain+1):
                if i == originalN or (remain - i) in memo:
                    continue
                m= max(m,dfs(remain - i, prod * i))
            
            
            return m
            
            memo[(remain)] = m
        
        return dfs(n,1)