class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        #lands = []
        #water = []
        m,n = len(grid),len(grid[0])
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    q.append([r,c])
               
        
        if len(q) == 0 or len(q) == n * m:
            return -1
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        level = -1
        #seen = set()
        while q:
            
            for i in range(len(q)):
                
                r,c = q.popleft()
                
                for x,y in directions:
                    nx,ny = x + r, y + c
                    
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] == 1:
                        continue
                    
                    grid[nx][ny] = 1
                    q.append([nx,ny])

            level +=1
        return level