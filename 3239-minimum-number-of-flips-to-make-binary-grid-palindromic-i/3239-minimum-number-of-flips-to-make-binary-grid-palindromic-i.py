class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        
        rows = 0
        cols = 0
        for i in range(len(grid)):
            
            for j in range(len(grid[i])//2):
                
                v1 = grid[i][-j-1]
                v2 = grid[i][j]
                

                if v1 != v2:
                    rows += 1
                    
     
                    
        for i in range(len(grid[0])):
            
            for j in range(len(grid)//2):

                v3 = grid[-j-1][i]
                v4 = grid[j][i]
                    
                if v3 != v4:
                    cols += 1
        return min(rows,cols)
            
            

            
        