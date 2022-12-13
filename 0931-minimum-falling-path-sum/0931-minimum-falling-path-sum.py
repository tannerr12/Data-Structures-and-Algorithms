class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        
        dp = [[0 for j in range(len(matrix[0]) +1)] for i in range(len(matrix))]
        
        
        for i in range(len(dp)):
            dp[i][-1] = float('inf')
        
        for j in range(len(dp[0]) -2,-1,-1):
            dp[-1][j] = matrix[-1][j]
        
        for i in range(len(matrix) -2, -1 , -1):
            
            for j in range(len(matrix[i]) -1,-1,-1):
                
                dp[i][j] = matrix[i][j] + min(dp[i+1][j], dp[i+1][j-1], dp[i+1][j+1])
                
        res = float('inf')
        
        for j in range(len(matrix[0])):
            res = min(dp[0][j], res)
            
        return res