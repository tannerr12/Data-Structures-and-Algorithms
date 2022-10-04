class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        
        
        dp = {}
        
        
        
        def dfs(r,c):
            if r >= len(triangle) or r < 0 or c >= len(triangle[r]) or c < 0:
                return float('inf')
            
            if r == len(triangle)-1:
                return triangle[r][c]
            
            
            if (r,c) in dp:
                return dp[(r,c)]
            #check 2 directions
            
            dp[(r,c)] = min(dfs(r+1,c), dfs(r+1,c+1)) + triangle[r][c]
            
            
            return dp[(r,c)]
            
            
            

        return dfs(0,0)
                
        
        
        