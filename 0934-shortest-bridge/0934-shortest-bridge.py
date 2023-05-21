class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        islands = set()
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        gset = set()
        def dfs(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0 or (i,j) in seen:
                return 0
            
            seen.add((i,j))
            gset.add((i,j))
            for x,y in directions:
                dfs(i+x,j+y)
        
        #group islands
        count = 1
        first = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1 and (i,j) not in gset:
                    if not first:
                        first = (i,j)
                    seen = set()
                    dfs(i,j)
                    for val in seen:
                        islands.add((val[0],val[1], count))
                    
                    count +=1
                    

        #bfs
        q= []
        q.append((0,first[0],first[1]))
        seen = set()
        seen.add((first[0],first[1]))
        #res = float('inf')
        while q:
            c,i,j = heappop(q)
            if (i,j,2) in islands:
                return c -1
            for x,y in directions:
                if i+x < 0 or i+x >= len(grid) or j+y < 0 or j + y >= len(grid[0]) or (i+x,j+y) in seen:
                    continue
                seen.add((i+x,j+y))
                if (i+x, j+y, 1) in islands:
                    heappush(q, (0,i+x,j+y))
                else:
                    heappush(q, (c + 1,i+x,j+y))
        
        return -1
                    
                
                
                
                
        
        
            
            