class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        
        @cache
        def dfs(val):
            
            if val == 0:
                return 0
            
            res =float('inf')
            for i in range(k,val+1,10):
                res = min(res,dfs(val - i) +1)

            
            return res
        
        
        if k == 0:
            k = 10
        res = dfs(num)
        
        return res if res != float('inf') else -1