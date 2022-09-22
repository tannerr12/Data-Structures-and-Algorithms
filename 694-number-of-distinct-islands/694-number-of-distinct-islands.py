class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        
        
        def dfs(r,c):
       
            if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0 or grid[r][c] != 1:
              
                return 
            
            grid[r][c] = 0
            
            checkIsland.add((r - rorgin,c-corgin))
            #check 4 directions
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1) 
            
            
        res = 0
        temp = set()
        for r in range(len(grid)):
            
            for c in range(len(grid[0])):
                
                if grid[r][c] == 1:
                    checkIsland = set()
                    rorgin = r
                    corgin = c
                    dfs(r,c)
                    
                    if checkIsland not in temp:
                        temp.add(frozenset(checkIsland))
                        res +=1
                    
        
  
        return res