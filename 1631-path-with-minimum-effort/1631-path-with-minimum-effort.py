class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        m,n = len(heights),len(heights[0])
        heap = [(0,[0,0])]
        directions = [[1,0],[0,1], [-1,0],[0,-1]]
        seen = set()
 
        while heap:
            
            cost, pair = heappop(heap)
            
            x,y = pair
            if (x,y) in seen:
                continue
            if x == m-1 and y == n -1:
                return cost
            seen.add((x,y))
            
            for nx,ny in directions:
                newx,newy= x + nx, y + ny
                
                if newx >= m or newx <0 or newy >= n or newy < 0 or (newx,newy) in seen:
                    continue
                
                
                c = max(cost, abs(heights[x][y] - heights[newx][newy]))
                
                heappush(heap, (c, [newx,newy]))
                
        
        
            