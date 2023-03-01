class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        directions = [[0,1], [-1,0], [0,-1], [1,0]]
        
        m = len(grid)
        n = len(grid[0])
        q = deque()
        seen = set()
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == '*':
                    q.append((i,j))
                    seen.add((i,j))
        
        
        dist = 0
        while q:
            
            for i in range(len(q)):
                
                x,y = q.popleft()
                if grid[x][y] == '#':
                    return dist
                for a,b in directions:
                    nx,ny = x+a, y+b
                    
                    if nx >= m or nx < 0 or ny >= n or ny < 0 or (nx,ny) in seen or grid[nx][ny] == 'X':
                        continue
                        
                    seen.add((nx,ny))
                    q.append((nx,ny))
        
            
            dist +=1
        
        return -1