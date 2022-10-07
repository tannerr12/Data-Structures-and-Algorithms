perfectSquareSet = []
p = set()
class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [n] * (n+1)
        dp[0] = 0
        for target in range(1,n+1):
            for i in range(1,target+1):

                s = i * i
                if target - s < 0:
                    break
                    
                dp[target] = min(dp[target], 1 + dp[target - s])

        
        
        #print(dp)
        return dp[n]

        
        
        
        