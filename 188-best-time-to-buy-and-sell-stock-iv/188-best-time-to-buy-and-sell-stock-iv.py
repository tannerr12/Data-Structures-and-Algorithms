class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [0] * len(prices)
        

        for i in range(k):
            curr = -prices[0] 
            m = 0
            for i in range(1,len(prices)):
                curr = max(curr, dp[i] -prices[i])
                m= max(m,prices[i] + curr)
                dp[i] = m


        
        print(dp)
        return dp[-1]
            