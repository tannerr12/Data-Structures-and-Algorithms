class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        directions = [[-1,0], [1,0], [0,-1], [0, 1]]
        q = deque([start])
        heap = []
        dist = 1
        s = grid[start[0]][start[1]]
        ans = []
        if s >= pricing[0] and s <= pricing[1]:
            ans.append([0,s,start[0], start[1]])
        
        grid[start[0]][start[1]] = 0
        
        while q:
            
            for i in range(len(q)):
                
                x,y = q.popleft()
                for a,b in directions:
                    newx,newy = x + a, y + b
                    
                    if newx < 0 or newy < 0 or newx >= m or newy >= n or grid[newx][newy] == 0:
                        continue
                        
                    if grid[newx][newy] >= pricing[0] and grid[newx][newy] <= pricing[1]:
                        ans.append([dist, grid[newx][newy], newx, newy])                        
                    
                    grid[newx][newy] = 0
                    q.append([newx,newy])
                    
            if len(ans) >= k:
                break
            dist += 1
        ans.sort()
        newans = []
        
        for a,b,c,d in ans:
            newans.append([c,d])
            k-=1
            if k == 0:
                break
        
        return newans