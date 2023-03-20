class Solution:
    def integerReplacement(self, n: int) -> int:
        
        @cache
        def dfs(num):
            
            if num == 1:
                return 0
            
            res = float('inf')
            #if even always // 2
            if num % 2 == 0:
                res = min(res, dfs(num // 2) + 1)
            #else if odd we take 2 paths
            else:
                
                res = min(res,dfs(num - 1) + 1)
                res = min(res,dfs(num + 1) + 1)
            
            return res
        
        return dfs(n)