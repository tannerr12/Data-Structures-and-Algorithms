
class Solution:
    def numSquares(self, n: int) -> int:
        if math.sqrt(n) % 1 == 0: return 1 

        dp = [float('inf') for i in range(n+1)]
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            if math.sqrt(i) % 1 == 0:
                dp[i] = 1
                continue
            mult = 1
            while mult * mult <= i:

                #this will be our dp target  
                target = i - (mult * mult)
          
                dp[i] = min(1 + dp[target], dp[i])
                if dp[i] == 2:
                    break
                mult +=1
        

        return dp[n]



            




        
        
        
        