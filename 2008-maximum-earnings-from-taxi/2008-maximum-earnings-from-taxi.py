class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        
        rides = sorted(rides,key = lambda x:x[1])
        
        #print(rides)
        dp = [0] * (n + 1)
        
        
        idx = 0
        
        for i in range(1,n+1):
            dp[i] = dp[i-1] 
            while idx < len(rides) and rides[idx][1] == i:
                dp[i] = max(dp[i], dp[rides[idx][0]] + (rides[idx][1] - rides[idx][0]) + rides[idx][2])
                #print(dp[i])
                idx += 1
            
        
        
       
        return dp[-1]
            
            