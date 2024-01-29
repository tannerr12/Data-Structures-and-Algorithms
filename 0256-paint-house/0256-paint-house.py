class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        #top down
        @cache
        def Paint(i, cost, parent):

            if i >= len(costs):
                return cost
            

            #paint 3 colors
            m = float('inf')
            for j in range(3):
                if j == parent:
                    continue
                m  = min(m,Paint(i+1, cost + costs[i][j], j))

            

            return m

        
        #return Paint(0,0, -1)
        

        #bottom up

        dp = [[float('inf') for j in range(3)] for i in range(len(costs))]
        
        for j in range(3):
            dp[0][j] = costs[0][j]
        for i in range(1,len(costs)):
            for j in range(3):
                for k in range(len(dp[i-1])):
                    if k == j:
                        continue
                    dp[i][j] = min(dp[i-1][k] + costs[i][j], dp[i][j])
        

        print(dp)
        return min(dp[-1])
