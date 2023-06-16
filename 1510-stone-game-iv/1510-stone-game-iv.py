class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        if sqrt(n) % 1 == 0:
            return True
        
        @cache
        def dfs(stones):
            
            if stones == 0:
                return False

            res = 0
            
            res = False
            mn = 1
            while mn * mn <= stones:
                res = res or (not dfs(stones - (mn * mn)))
                mn +=1
                
            
            return res
        
        return dfs(n)
                
            