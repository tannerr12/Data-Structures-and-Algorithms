class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        m,n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        dpH = [[0 for j in range(n)] for i in range(m)]
        dpr = [[0 for j in range(n)] for i in range(m)]
        left = [[0 for j in range(n)] for i in range(m)]
        right = [[n-1 for j in range(n)] for i in range(m)]
        
        
        res = 0 
        def oob(i,j,dp):
            
            if (i < 0 or j < 0 or j >= len(matrix[0])):
                return 0
            else:
                return dp[i][j]
            
        for i in range(m):
            lstack = []
            rstack = []
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + oob(i,j-1,dp)
                    dpH[i][j] = 1 + oob(i-1, j,dpH)      
                
                
                while lstack and dpH[i][lstack[-1]] >= dpH[i][j]:
                    lstack.pop()
                
                if lstack:
                    left[i][j] = lstack[-1] + 1
                
                lstack.append(j)
            
            for j in range(n-1,-1,-1):
                if matrix[i][j] == "1":
                    dpr[i][j] = 1 + oob(i,j+1,dpr)
                    
                while rstack and dpH[i][rstack[-1]] >= dpH[i][j]:
                    rstack.pop()
                
                if rstack:
                    right[i][j] = rstack[-1] - 1
                
                rstack.append(j)
                
        
      
        for i in range(m):
            for j in range(n):    
                res = max(res, (1 + min(right[i][j], j + dpr[i][j] -1) - max(left[i][j], j - dp[i][j] + 1)) * dpH[i][j])
        return res