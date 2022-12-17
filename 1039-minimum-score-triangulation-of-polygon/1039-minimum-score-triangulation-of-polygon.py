class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        n  = len(values)
        dp = [[0 for j in range(n)] for i in range(n)]
        
        
        for l in range(2,n):
            
            for left in range(0,n-l):
                
                right = left + l
                
                dp[left][right] = float('inf')
                
                for k in range(left +1,right):
                    dp[left][right] = min(dp[left][right], dp[left][k] + dp[k][right] + values[left] * values[k] * values[right])
        
        
        return dp[0][-1]