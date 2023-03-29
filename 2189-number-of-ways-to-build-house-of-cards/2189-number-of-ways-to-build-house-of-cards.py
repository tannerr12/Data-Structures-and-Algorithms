class Solution:
    def houseOfCards(self, n: int) -> int:
        
        
        @cache
        def dfs(rem, prev):
            
            if rem == 0:
                return 1
            
            res = 0
            i = 2
            while i <= prev - 3 and i <= rem:
                
                res += dfs(rem - i, i)
                i += 3
            
            
            return res
        
        return dfs(n, n+3)