class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        

        @cache
        def dfs(i):
            
            if i >= len(prices):
                return 0
            elif i >= len(prices) // 2:
                return prices[i]
            
            res = float('inf')
            
            #take 
            for j in range(i+1, i*2+3):
                res = min(res, dfs(j) + prices[i])

                
            
            return res
        
        
        return dfs(0)