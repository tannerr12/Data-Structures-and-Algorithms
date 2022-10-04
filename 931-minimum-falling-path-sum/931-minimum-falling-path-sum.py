class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = {}
        
        
        res = float('inf')
        
        def dfs(r,c):
            if r >= len(matrix) or r < 0 or c >= len(matrix[0]) or c < 0:
                return float('inf')
            
            if r == len(matrix)-1:
                return matrix[r][c]
            
            if (r,c) in dp:
                return dp[(r,c)]
            #check 3 directions
            
            m = min(dfs(r+1,c-1),
            dfs(r+1,c),
            dfs(r+1,c+1)) + matrix[r][c] 
            
            
            dp[(r,c)] = m
            
            return m
            
            
                
            
            
        for c in range(len(matrix)):
            
            res = min(res,dfs(0,c))
        
        
        return res
        
        
        
            
        
        
        