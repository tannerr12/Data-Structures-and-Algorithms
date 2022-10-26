class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        
        
        res = float('inf')
        empty = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        
        fgrid = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
     
        q = deque()    
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
               
                if grid[i][j] == 1:
                    localres = float('inf')
                    distance = 0
                    q.append((i,j,distance))
                    
                    
                    while q:
                        
                        r,c,d = q.popleft()
                        
                        for x,y in directions:
                            if r + x >= 0 and r + x < len(grid) and c + y >= 0 and c + y < len(grid[0]) and grid[r+x][c + y] == empty:
                                fgrid[r+x][c+y] += d +1
                                grid[r+x][c+y] -=1
                                q.append((r+x,c+y, d+1))
                                localres = min(localres, fgrid[r+x][c+y])
                    
                    res = localres
                    empty -=1
                                    
        
        
        
        
        if res == float('inf'):
            res = -1
           
        return res