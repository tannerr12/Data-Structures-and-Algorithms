class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        countzero = 0
        start = [0, 0]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                
                if grid[r][c] == 0:
                    countzero+=1
                elif grid[r][c] == 1:
                    start = [r,c]
                    
        #memo = {}
       # @cache
        def dfs(r,c,count):
            
            if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0 or grid[r][c] == -1:
                return 0
            
            if grid[r][c] == 2 and count == -1:
                return 1
            elif grid[r][c] == 2 and count != -1:
                return 0
            
            #4 directions
            
            res = 0
            v = grid[r][c]
            grid[r][c] = -1
           # s = str(grid)
            res += dfs(r+1,c,count -1)
            res += dfs(r-1,c,count -1)
            res += dfs(r,c+1,count -1)
            res += dfs(r,c -1, count -1)
            grid[r][c] = v
            
            return res
        
        
        
        
        return dfs(start[0], start[1], countzero)