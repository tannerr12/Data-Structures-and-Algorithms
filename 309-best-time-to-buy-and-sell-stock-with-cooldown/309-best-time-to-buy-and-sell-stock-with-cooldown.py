class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}
        def dfs(i, b):
            
            if i >= len(prices):
                return 0
            if (i,b) in dp:
                return dp[(i,b)]
            if b:
                buy = dfs(i+1, not b) - prices[i]
                cooldown = dfs(i+1,b)
                dp[(i, b)] = max(buy,cooldown)
            else:
                sell = dfs(i+2, not b) + prices[i]
                cooldown = dfs(i+1,b)
                dp[(i, b)] = max(sell,cooldown)
     
            
          
            
            return dp[(i,b)]
        
        
        
        
        return dfs(0,True)