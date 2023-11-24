class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        
        
        #use tarjans to group strongly connected components aka islands 
        #if islands is > 1 we have disconnected the island
        
        #there are 900 tiles total so we can n2 the solution
        #worst case should be 30 iterations
        #900 * 900 * 30 = 24m (too big)
        #what if we only try diaganols and check if the there is an island above + left and below + right
        #we could try all of them which should be around 30 * 4 iterations 120 and attempt the diags which should be 
        #around 30 iterations
        #we can use math such that our best score will be our cheapest diaganol that satisfies both conditions or the count of islands in the grid
        #we can check if the grid is intially strongly connected with Tarjan but anything will work
        
        #todo 
        #add bottom to top on the right side and left -> right bottom row 
        def tarjan(i,j):
            nonlocal idVal,islands
            
            ids[(i,j)] = idVal
            inStack[(i,j)] = True
            stack.append((i,j))
            lowVal[(i,j)] = idVal
            idVal += 1
            
            for x,y in directions:
                newx, newy = i + x, j + y
                if newx < 0 or newy < 0 or newx >= m or newy >= n or grid[newx][newy] == 0:
                    continue
                
                if ids[(newx,newy)] == -1:
                    tarjan(newx,newy)
                
                if inStack[(newx,newy)]:
                    lowVal[(i,j)] = min(lowVal[(i,j)], lowVal[(newx,newy)])
            
            if lowVal[(i,j)] == ids[(i,j)]:
                
                while stack:
                    
                    x,y = stack.pop()
                    inStack[(x,y)] = False
                    lowVal[(x,y)] = ids[(i,j)]
                    if (x,y) == (i,j):
                        break
                
                islands += 1
                
        def tarjanCheck(i,j,si,sj):
            nonlocal idVal,islands
            
            ids[(i,j)] = idVal
            inStack[(i,j)] = True
            stack.append((i,j))
            lowVal[(i,j)] = idVal
            idVal += 1
            
            for x,y in directions:
                newx, newy = i + x, j + y
                if newx < 0 or newy < 0 or newx >= m or newy >= n or grid[newx][newy] == 0 or (newx, newy) == (si,sj):
                    continue
                
                if ids[(newx,newy)] == -1:
                    tarjanCheck(newx,newy,si,sj)
                
                if inStack[(newx,newy)]:
                    lowVal[(i,j)] = min(lowVal[(i,j)], lowVal[(newx,newy)])
            
            if lowVal[(i,j)] == ids[(i,j)]:
                
                while stack:
                    
                    x,y = stack.pop()
                    inStack[(x,y)] = False
                    lowVal[(x,y)] = ids[(i,j)]
                    if (x,y) == (i,j):
                        break
                
                
        

        directions = [[-1,0], [1,0], [0,-1],[0,1]]
        m,n = len(grid), len(grid[0])
        ids = defaultdict(lambda:-1)
        inStack = defaultdict(bool)
        stack = []
        idVal = 0
        lowVal = defaultdict(int)
        islands = 0
        lands = 0
        landls = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    landls.append((i,j))     
                if grid[i][j] == 1 and ids[(i,j)] == -1:
                    tarjan(i,j)
        
        
        if len(landls) == 1:
            return 1
        if islands > 1 or islands == 0:
            return 0
        
        for x,y in landls:
            ids = defaultdict(lambda:-1)
            inStack = defaultdict(bool)
            lowVal = defaultdict(int)
            idVal = 0
            stack = []
            checked = False
            for a,b in directions:
                newx,newy = x + a, y + b
                if newx < 0 or newy < 0 or newx >= m or newy >= n or grid[newx][newy] == 0:
                    continue
                
                if ids[(newx,newy)] == -1:        
                    if checked:
                        return 1
                    checked = True
                    tarjanCheck(newx,newy,x,y)
                
            
        
        #print(islands, lands)

        
        return 2


    
    