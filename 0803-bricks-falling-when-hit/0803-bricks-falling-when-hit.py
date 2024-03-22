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
                            
                        union((nx,ny), (i,j))
        
        
        
        lastSize = 0
        sadded = set()
        #check the size of the top row
        for j in range(len(grid[0])):
            par = find((0,j))
            if grid[0][j] == 1 and par not in sadded:
                lastSize += groupSize[par]
                sadded.add(par)
            
        
        ans = [0] * len(hits)
        for i in range(len(hits)-1,-1,-1):
            x,y = hits[i]
            if grid[x][y] == 0:
                continue
            
            if x == 0:
                sadded.add((x,y))
                
            grid[x][y] = 1
            parent[(x,y)] = (x,y)
            groupSize[(x,y)] = 1
            
            for a,b in directions:
                nx,ny = x + a, y + b
                if checkOOB(nx,ny):
                    union((x,y), (nx,ny))
            
            size = 0
            added = set()
            #check the size of the top row
            for val in sadded:
                par = find(val)
                if par not in added:
                    size += groupSize[par]
                    added.add(par)
                
            
            sadded = added
            ts = size
            if find((x,y)) in added:
                size -= 1
        
            ans[i] = size - lastSize
            
            lastSize = ts
        
        return ans
            
                    
                
            
            
            
             
            
        
        
        
        
                    
        
        