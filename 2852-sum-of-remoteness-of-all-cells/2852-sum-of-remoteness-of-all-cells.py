class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        '''
        parent = [i for i in range((len(grid)+1) * (len(grid)+ 1))]
        rank = [0 for i in range((len(grid)+1) * (len(grid) + 1))]
        
        
        def find(x):
            
            if x == parent[x]:
                return parent[x]
            
            parent[x] = find(parent[x])
            
            return parent[x]
        
        
        def union(x,y):
            
            x1,y1 = find(x), find(y)
            
            if x1 != y1:
                
                if rank[x1] > rank[y1]:
                    parent[y1] = x1
                elif rank[y1] > rank[x1]:
                    parent[x1] = y1
                    
                else:
                    rank[x1] += 1
                    parent[y1] = x1
                    
            
        
        total = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != -1:
                    total += grid[i][j]
                    newi,newj = i + 1, j + 1
                    if i > 0 and grid[i-1][j] != -1:
                        union(newi * newj, (i) * newj)
                    
                    if j > 0 and grid[i][j-1] != -1:
                        union(newi*newj, newi * (j))
                        
        
        for i in range(len(parent)):
            find(i)
            
        
        for i in range(len(grid)):
            for j in range(len(grid[0]))
        print(parent)
                        
        '''
        total = 0
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != -1:
                    total += grid[i][j]
        
        
        def bfs(i,j):
            
            score = 0
            size = 0
            q = deque([[i,j]])
            seen.add((i,j))
            while q:
                
                for i in range(len(q)):
                    
                    x,y = q.popleft()
                    score += grid[x][y]
                    size += 1
                    for a,b in directions:
                        nx,ny = a + x, b + y
                        
                        if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] == -1 or (nx,ny) in seen:
                            continue
                            
                        seen.add((nx,ny))
                        q.append([nx,ny])
                        
            
            return score,size
        
        
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in seen and grid[i][j] != -1:
                    s,si = bfs(i,j)
                    res += (total - s) * si
        return res