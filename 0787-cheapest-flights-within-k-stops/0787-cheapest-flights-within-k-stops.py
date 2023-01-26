class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        dp = [float('inf')] * (n)

        dp[src] = 0
            

        for i in range(k+1):
            cur=dp[:]
            for f,t,p in flights:
                if dp[f] + p < cur[t]:
                    cur[t] = dp[f] + p
            dp = cur[:]



        return dp[dst] if dp[dst] != float('inf') else -1