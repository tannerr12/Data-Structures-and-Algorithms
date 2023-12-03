class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        @lru_cache(maxsize=100)
        def dfs(val, i):
            
            if val > n:
                return False
            elif val == n:
                return True
            elif i > 16:
                return False
            
            res = False
            #take 
            res = res or dfs(val + 3 ** i, i+1)
            #dont take
            res = res or dfs(val, i+1)
            
            return res
        
        return dfs(0, 0)
        
        
        
        