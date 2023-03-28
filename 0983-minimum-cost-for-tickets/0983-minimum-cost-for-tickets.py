class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
       
        dp = [0 for i in range(366)]
        m = days[-1]
        days = set(days)
        def minPrice(i):

            if i > 365:
                return 0
            if i in days:
                dp[i] = min(dp[i-1] + costs[0],dp[max(i-7, 0)] + costs[1], dp[max(i-30, 0)] + costs[2])
            else:
                dp[i] = dp[i -1]
            
            minPrice(i+1)

            return dp[i]
        

     

       # for i in range(costs):

        r = minPrice(1)
        #print(r)
        return dp[m]

        dp = [[0] for i in range(days[-1] +1)]
        dp[0] = 0
        d = set(days)
        for i in range(1, days[-1] +1):
            one , two , three = costs[0],costs[1],costs[2]
            #one
            if i-1 >=0:
                one = dp[i-1] + costs[0]
      
            if i - 7 >= 0:
                two = dp[i-7] + costs[1]
     
            if i - 30 >= 0:
                three = dp[i-30] + costs[2]
           
            if i in d:
                dp[i] = min(one,two,three)
            else:
                dp[i] = dp[i-1]
        
        return dp[-1]

         #if i in days:
         #       dp[i] = min(dp[max(i-1,0)]+costs[0],dp[max(i-7,0)]+costs[1],dp[max(i-30,0)]+costs[2])
         #   else:
         #       dp[i]=dp[i-1]

