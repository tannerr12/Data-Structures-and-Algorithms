class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        #all that matters is that a brick must be connected to the top
        #what if we do this in reverse? we count the number of bricks connected to the top after all deletes
        #than we union the bricks back on and say the impact is newbricks - oldbricks total? we only have to check the top row of bricks
        #the union would union the new brick in 4 directions where there are other bricks 
        #if the new brick connects with a brick stack that is still not at the top than the impact would be 0
        
        
        rank = defaultdict(int)
        parent = defaultdict(int)
        groupSize = defaultdict(lambda:1)
        
        def find(x):
            
            if x == parent[x]:
                return parent[x]
            
            parent[x] = find(parent[x])
            
            return parent[x]
        
        
        def union(x,y):
            
            p1,p2 = find(x), find(y)
            
            if p1 != p2:
                
                if rank[p1] > rank[p2]:
                    parent[p2] = p1
                    groupSize[p1] += groupSize[p2]
                    groupSize[p2] = 0
                elif rank[p2] > rank[p1]:
                    parent[p1] = p2
                    groupSize[p2] += groupSize[p1]
                    groupSize[p1] = 0
                else:
                    if p2 == 0:
                        parent[p1] = p2
                        rank[p2] += 1
                        groupSize[p2] += groupSize[p1]
                        groupSize[p1] = 0
                    else:
                        parent[p2] = p1
                        rank[p1] += 1
                        groupSize[p1] += groupSize[p2]
                        groupSize[p2] = 0
            
        
        
        for x,y in hits:
            if grid[x][y] == 1:
                grid[x][y] = 2
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def checkOOB(x,y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != 1:
                return False
            return True
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 1:
                    continue
                    
                if (i,j) not in parent:
                    parent[(i,j)] = (i,j)
                    groupSize[(i,j)] = 1
                    
                for x,y in directions[:2]:
                    nx,ny = i+x,j+y
                    if checkOOB(nx,ny): 
                        if (nx,ny) not in parent:
                            parent[(nx,ny)] = (nx,ny)
                            groupSize[(nx,ny)] = 1
                        
                        if nx == 0:
                            union(0, (i,j))
                        
                        elif i == 0:
                            union(0, (nx,ny))
                            
                        else:
                            union((nx,ny), (i,j))
        
        
        
        lastSize = 0
        sadded = set()
       
        par = find(0)
        lastSize += groupSize[par]
       
            
            
        
        ans = [0] * len(hits)
        for i in range(len(hits)-1,-1,-1):
            x,y = hits[i]
            if grid[x][y] == 0:
                continue
            

                
            grid[x][y] = 1
            parent[(x,y)] = (x,y)
            groupSize[(x,y)] = 1
            
            if x == 0:
                union((x,y), 0)            
            
            for a,b in directions:
                nx,ny = x + a, y + b
                if checkOOB(nx,ny):
                    if nx == 0:
                        union((x,y), 0)
                    else:    
                        union((x,y), (nx,ny))
            
            size = 0
            #added = set()
            #check the size of the top row
            #for val in sadded:
            #    par = find(val)
            #    if par not in added:
            #        size += groupSize[par]
            #        added.add(par)
            size += groupSize[find(0)]    
            
            ts = size
            if find((x,y)) == find(0):
                size -= 1
        
            ans[i] = size - lastSize
            
            lastSize = ts
        
        return ans
            
                    
                
            
            
            
             
            
        
        
        
        
                    
        
        