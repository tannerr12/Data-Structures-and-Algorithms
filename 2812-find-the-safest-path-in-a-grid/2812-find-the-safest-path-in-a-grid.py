class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        
        #avoid all theifs since the ans will be 0
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        
        res = 0
       
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        theifs = deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):        
                if grid[i][j] == 1:
                    theifs.append((i,j))
                    
        @cache
        def getTheifCost(x,y):
            mn = float('inf')
            for a,b in theifs:
                mn = min(mn, abs(a-x) + abs(y-b))
            
            return mn
        
        theifCache = {}
        level = 0
        while theifs:
            
            for i in range(len(theifs)):
                
                x,y = theifs.popleft()
                
                if (x,y) not in theifCache:
                    theifCache[(x,y)] = level
                else:
                    continue
                    
                for a,b in directions:
                    newx,newy = x + a, y + b
                    if newx < 0 or newx >= len(grid) or newy < 0 or newy >= len(grid[0]) or grid[newx][newy] == 1 or (newx,newy) in theifCache:
                        continue
                    
                    theifs.append((newx,newy))
                
        
            level +=1
            
        q = [(-getTheifCost(0,0),0,0)]        
        gridcache = {}
        gridcache[(0,0)] = q[0][0]
        
        while q:

            cost, x, y = heappop(q)

            #if (x,y) in gridcache and gridcache[(x,y)] >= cost:
            #    continue


            cost = max(cost, -theifCache[(x,y)])


            if [x,y] == [len(grid)-1, len(grid[0])-1]:
                return -cost
               

                
            for a,b in directions:
                newx,newy = x + a, y + b

                if newx < 0 or newx >= len(grid) or newy < 0 or newy >= len(grid[0]) or grid[newx][newy] == 1 or ((newx,newy) in gridcache and gridcache[(newx,newy)] <= cost) or cost >= res:
                    continue
                gridcache[(newx,newy)] = cost
                heappush(q, (cost,newx,newy))

        
        return -res
                