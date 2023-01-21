class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        heap = []
        heappush(heap, (0,[0,0]))
        
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        seen = set()
        
        while heap:
            
            cost, pack = heappop(heap)
            x,y = pack
            if [x,y] == [m-1,n-1]:
                return cost
            seen.add((x,y))
            
            for up,right in directions:
                newx = up + x
                newy = right + y
                
                if (newx, newy) in seen:
                    continue
                if newx >= m or newx < 0 or newy >= n or newy < 0:
                    continue
                if grid[newx][newy] == 1:
                    cost +=1
                seen.add((newx,newy))
                heappush(heap, (cost,[newx,newy]))
                if grid[newx][newy] == 1:
                    cost -=1
                
        return res
            
        
        
        
        