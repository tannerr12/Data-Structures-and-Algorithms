class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        grid = [[0 for j in range(n)] for i in range(n)]
        
        count = 1
        i, j = 0,0
        offset = 0
        while count < (n * n) + 1:
            
            while i < len(grid) and j < len(grid[i]) and grid[i][j] == 0:
                grid[i][j] = count
                count +=1
                j +=1
            
            
            j -= 1
            i +=1
            
            while i < len(grid) and j < len(grid[i]) and grid[i][j] == 0:
                grid[i][j] = count
                count +=1
                i+=1
            
            i -=1
            j -= 1
            
            while i >= 0 and j >= 0 and grid[i][j] == 0:
                grid[i][j] = count
                count +=1
                j -=1
            
            i-=1
            j +=1
            
            while i >= 0 and j >= 0 and grid[i][j] == 0:
                grid[i][j] = count
                count +=1
                i -=1
            
            i +=1
            j +=1
            
        
        
        
        
        
        
        
        return grid
        
        