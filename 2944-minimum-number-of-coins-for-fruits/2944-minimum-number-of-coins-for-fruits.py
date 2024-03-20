class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        
        @cache
        def dfs(i,free):
            
            if i + free >= len(prices):
                return 0
            
            res = float('inf')
            
            #take 
            res = min(res, dfs(i+1, i+1) + prices[i])
            
            #skip
            if free > 0:
                res = min(res, dfs(i+1, max(0, free - 1)))
                
            
            return res
        
        
        return dfs(0,0)