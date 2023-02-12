class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        islandCount = 0
        def findIsland(r,c,grid):
            if (0 > r or r > height -1) or (0 > c or c > width -1) or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            
            findIsland(r+1, c, grid)  
            findIsland(r-1, c, grid)  
            findIsland(r, c+1, grid)  
            findIsland(r, c-1, grid)  
            
        for r in range(height):
            for c in range(width):
                if grid[r][c] == "1":
                    findIsland(r,c,grid)
                    islandCount += 1
        
        

        
        
        return islandCount