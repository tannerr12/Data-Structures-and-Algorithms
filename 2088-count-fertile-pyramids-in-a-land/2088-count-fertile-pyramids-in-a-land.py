class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        
        R = len(grid)
        C = len(grid[0])
        
        def go(grid):
            
            LU = [[0] * C for _ in range(R)]
            RU = [[0] * C for _ in range(R)]
            
            #check up and left
            for i in range(1, R):
                for j in range(1, C):
                    if grid[i][j] == 1 and grid[i-1][j] == 1 and grid[i][j-1] == 1:
                        LU[i][j] = min(LU[i-1][j], LU[i][j-1]) + 1
            
            #check up and right
            for i in range(1, R):
                for j in range(C -2, -1,-1):
                    if grid[i][j] == 1 and grid[i-1][j] == 1 and grid[i][j+1] == 1:
                        RU[i][j] = min(RU[i-1][j], RU[i][j+1]) + 1
            
            count = 0
            for i in range(R):
                for j in range(C):
                    count += min(LU[i][j], RU[i][j])
            
            return count
        
        
        res = 0 
        
        res += go(grid)
        
        grid = grid[::-1]
        
        res += go(grid)
        
        return res