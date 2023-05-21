class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        first = (0,0)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    first = (i,j)
                    break
                    
        #dijkstra
        q = [(0,first[0],first[1])]
        seen = set([(first[0],first[1])])
        
        while q:
            c,i,j = heappop(q)
            for x,y in directions:
                if i+x < 0 or i+x >= len(grid) or j+y < 0 or j+y >= len(grid[0]) or (i+x,j+y) in seen:
                    continue
                seen.add((i+x,j+y))
                if c == 0 and grid[i+x][j+y] == 1:
                    heappush(q, (0,i+x,j+y))
                elif c > 0 and grid[i+x][j+y] == 1:
                    return c
                else:
                    heappush(q, (c + 1,i+x,j+y))
        
    
                
                
                
                
        
        
            
            