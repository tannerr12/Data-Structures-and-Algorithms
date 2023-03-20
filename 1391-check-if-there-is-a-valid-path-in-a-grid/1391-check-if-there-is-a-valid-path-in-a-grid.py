class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        m,n = len(grid), len(grid[0])
        q = deque()
        
        q.append((0,0))
        
        adj = {1: [[0,-1],[0,1]], 2: [[1,0], [-1,0]], 3: [[0,-1], [1,0]], 4: [[0,1], [1,0]], 5:
              [[-1,0], [0,-1]], 6: [[-1,0], [0,1]]}
        
        pairs = {(0,1) : [1,3,5], (0,-1) : [1,4,6], (1,0) : [2,5,6], (-1,0) : [2,3,4]}
        seen = set()
        seen.add((0,0))
        while q:
            
             for i in range(len(q)):
                    
                    a,b = q.popleft()
                    
                    if (a,b) == (m-1,n-1):
                        return True
                    
                    for x,y in adj[grid[a][b]]:
                        
                        newx = a + x
                        newy = b + y
                        
                        if newx < 0 or newy < 0 or newx >= m or newy >= n or (newx,newy) in seen or grid[newx][newy] not in pairs[(x,y)]:
                            continue
                        
                        seen.add((newx,newy))
                        q.append((newx,newy))
                    
            
        return False