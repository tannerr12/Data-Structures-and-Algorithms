class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        
        dp = [[0 for i in range(len(mat[0]) +1)] for j in range(len(mat) +1)] 
              

        
    
        for i in range(1,len(dp)):
            curr = 0
            for j in range(1,len(dp[0])):
                curr += mat[i-1][j-1]
                above = dp[i -1][j]
                dp[i][j] = curr + above
                
        
        
        for r in range(1,len(mat) +1):
            for c in range(1, len(mat[0]) +1):
                
                starti, startj = max(1,r-k), max(1,c-k)
                endi,endj = min(len(mat), r +k), min(len(mat[0]), c + k)
                
                mat[r-1][c-1] = (dp[endi][endj] - ((dp[endi][startj-1] + dp[starti-1][endj]) - dp[starti-1][startj-1]))
        
                                          
                                         
        return mat
            
                