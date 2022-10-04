class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        dp = [0] * len(prices)
        for i in range(2):
            curr = -prices[0]
            profit = 0
            
            for i in range(1,len(prices)):
                curr = max(curr, dp[i] - prices[i])
                
                profit = max(profit, prices[i]+curr)
                
                dp[i] = profit
        
        
        return dp[-1]
            
            