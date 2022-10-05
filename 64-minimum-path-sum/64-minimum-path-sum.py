class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        
        
        for r in range(len(grid) -1,-1,-1):
            
            for c in range(len(grid[0]) -1, -1,-1):
                
                if r +1 >= len(grid) and c + 1 >= len(grid[0]):
                    continue
                elif r + 1 >= len(grid):
                    
                    grid[r][c] =grid[r][c+1] + grid[r][c]
                elif c+ 1 >= len(grid[0]):
                    grid[r][c] = grid[r+1][c] + grid[r][c]
                else:
                    grid[r][c] = min(grid[r][c+1], grid[r+1][c]) + grid[r][c]
        
        
        return grid[0][0]
                
        
        
      