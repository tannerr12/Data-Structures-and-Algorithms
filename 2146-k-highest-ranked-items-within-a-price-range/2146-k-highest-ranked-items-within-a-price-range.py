class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        directions = [[-1,0], [1,0], [0,-1], [0, 1]]
        q = deque([start])
        heap = []
        dist = 0
        seen = set()
        seen.add((start[0], start[1]))
        while q:
            
            for i in range(len(q)):
                
                x,y = q.popleft()
                if grid[x][y] >= pricing[0] and grid[x][y] <= pricing[1]:
                    heappush(heap, [dist, grid[x][y], x, y])
                
                
                for a,b in directions:
                    newx,newy = x + a, y + b
                    
                    if newx < 0 or newy < 0 or newx >= m or newy >= n or grid[newx][newy] == 0 or (newx,newy) in seen:
                        continue
                        
                    seen.add((newx,newy))
                    q.append([newx,newy])
            dist += 1
        ans = []
        
        while k and heap:
            _, _1, x,y = heappop(heap)
            ans.append([x,y])
            k -= 1
        return ans