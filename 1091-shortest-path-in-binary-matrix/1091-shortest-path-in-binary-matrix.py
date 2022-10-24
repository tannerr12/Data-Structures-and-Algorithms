class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
      
        
        if grid[0][0] == 1:
            return -1
        
        
        
        q = deque()
        
        q.append((0,0))
        grid[0][0] = 1
        level = 1
        memo = {}
        directions = [[-1,0], [1,0], [0,-1], [0,1], [1,1], [1,-1], [-1,1], [-1,-1]];
        while q:
            
            for i in range(len(q)):
                r,c = q.popleft()
                if (r,c) in memo:
                    return memo[(r,c)]
                #grid[r][c] = level
                
                #memo[(r,c)] = level
                 
                if r== len(grid)-1 and c == len(grid[0]) -1:
                    return level
                for x,y in directions:
                    if r + x >= 0 and r + x < len(grid) and c + y >= 0 and c + y < len(grid[0]) and grid[r + x][c + y] == 0 and (r+x,c+y):
                        grid[r+x][c+y] = level + 1
                        q.append((r+x,c+y))                 
        
                
            
            
            
           
            level +=1

                 
        return -1
                
                