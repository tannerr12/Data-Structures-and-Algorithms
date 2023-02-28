class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] + 1 < grid[0][1] and grid[0][0] + 1 < grid[1][0]:
            return -1
        
        heap = []
        
        heap.append((0,0,0))
        seen = set()
        
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        while heap:
            
            t,r,c = heappop(heap)
            

            if (r,c) == (len(grid)-1, len(grid[0]) -1):
                return t
            seen.add((r,c))
            for x,y in directions:
                newr,newc = r + x, c + y
                
                if newr >= len(grid) or newr < 0 or newc >= len(grid[0]) or newc < 0 or (newr,newc) in seen:
                    continue

                if grid[newr][newc] > (t+1):
                    diff = abs((t + 1) - grid[newr][newc])
                    
                    check = math.ceil(diff / 2)
                    
                    heappush(heap, (t + (check * 2)+1, newr,newc))
                    seen.add((newr, newc))
                elif grid[newr][newc] <= (t+1):
                   
                    heappush(heap, (t + 1, newr,newc))
                    seen.add((newr, newc))
                
        return -1