class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        @cache
        def dfs(i):
            nonlocal n
            if i == n:
                return 0
            
            # take one
            res = stoneValue[i] - dfs(i + 1)
            
            
            #take two
            if i + 2 <= n:
                res = max(res, stoneValue[i] + stoneValue[i+1] - dfs(i+2))
            
            if i + 3 <= n:
                res = max(res, stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dfs(i+3))
            
            
            return res
            
        
        
        dif = dfs(0)
        if dif > 0:
            return "Alice"
        if dif < 0:
            return "Bob"
        return "Tie"