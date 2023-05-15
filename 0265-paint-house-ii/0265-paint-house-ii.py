class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        dp = [[float('inf') for j in range(len(costs[0]))] for i in range(len(costs))]
        
        for j in range(len(costs[0])):
            dp[0][j] = costs[0][j]
        for i in range(1,len(costs)):
            for j in range(len(costs[0])):
                for k in range(len(dp[i-1])):
                    if k == j:
                        continue
                    dp[i][j] = min(dp[i-1][k] + costs[i][j], dp[i][j])
        

        print(dp)
        return min(dp[-1])