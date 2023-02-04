class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        n,m = len(grid),len(grid[0])
        
        
        @cache
        def dfs(r1,c1,r2,c2):
            if r1 == n-1 and r2 == n-1 and c1 == m-1 and c2 == m-1:
                return True
                
            if r1 >= n or r2 >= n or c1 >=m or c2 >=m or grid[r1][c1] == 0 or grid[r2][c2] == 0 or (r1 == r2 and c1 == c2 and (r1 != 0 or c1 != 0)):
                return False
            

            
            #4 combinations
            res = False
            #down + right
            res = res or dfs(r1+1,c1,r2,c2+1)
            
            #right + down
            res = res or dfs(r1, c1 + 1, r2 + 1, c2)
            
            #down down
            res = res or dfs(r1+1,c1, r2+1,c2)
            
            #right right
            res = res or dfs(r1,c1+1, r2, c2+1)
        
            
            
            return res
        
    
        
        return not dfs(0,0,0,0)