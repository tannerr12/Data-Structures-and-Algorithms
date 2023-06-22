class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        seen = {}
        #seen[(0,0)] = grid[0][0]
        #q = deque()
        
        #q.append((0,0,grid[0][0]))
        
        res = 0
        '''
        while q:
            
            for i in range(len(q)):
                
                x,y,sc = q.popleft()
                if x == len(grid) - 1 and y == len(grid[0]) -1:
                    res = max(sc,res) 
                
                #if (x,y) in seen and sc <= seen[(x,y)] or sc <= res:
                #    continue
                    
                
                
                for k,c in directions:
                    newx,newy = x + k, y + c
                
                    if newx < 0 or newy < 0 or newx >= len(grid) or newy >= len(grid[0]) or ((newx,newy) in seen and min(sc,grid[newx][newy]) <= seen[(newx,newy)]):
                        continue
                    if grid[newx][newy] <= res:
                        continue
                        
                    seen[(newx,newy)] = min(sc,grid[newx][newy])
                    q.append((newx,newy,min(sc,grid[newx][newy])))
        
        
        
        return res
        
        '''
        
        heap = []
        
        heappush(heap, (-grid[0][0], 0, 0))
        
        while heap:
            
            sc,x,y = heappop(heap)
            sc = -sc
            
            if (x,y) in seen:
                continue
            
            if (x == len(grid)-1 and y == len(grid[0]) -1):
                return sc
            
            seen[(x,y)] = sc
            
            for k,c in directions:
                newx,newy = x + k, y + c

                if newx < 0 or newy < 0 or newx >= len(grid) or newy >= len(grid[0]) or (newx,newy) in seen:
                    continue
                
                heappush(heap, (-min(sc,grid[newx][newy]), newx, newy))
                
            
            
        
        