class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        
        

        
        if n == 1:
            return 0
        if n == 2:
            return 1
        
        
        @lru_cache(None)
        def dp(l,r):
            
            if l >= r:
                return 0
            
            res = float('inf')
            for k in range(l,r+1):
                
                a = dp(k+1,r) +k
                
                b = dp(l,k -1) + k
                
                
                res = min(res,max(a,b))
                
            return res
        
        return dp(1,n)

                