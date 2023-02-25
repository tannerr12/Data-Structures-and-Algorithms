class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit,maxProfit = float('inf'),0
        
        for i in range(len(prices)):
            
            profit = min(prices[i], profit)
            
            maxProfit = max(abs(profit - prices[i]),maxProfit)
            
        
        return maxProfit