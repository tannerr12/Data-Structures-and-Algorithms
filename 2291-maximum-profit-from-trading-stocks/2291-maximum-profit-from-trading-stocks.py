class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        
        dp = [0 for _ in range(budget + 1)]
        
        for p, f in zip(present, future):
            for i in range(budget, p - 1, -1):
             			    dp[i] = max(f - p + dp[i - p], dp[i])
                
        return dp[budget]