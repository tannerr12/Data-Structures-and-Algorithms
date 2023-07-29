class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        def oob(i,j):
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]):
                return True
            return False
            
        start = 0,0
        box = 0,0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'S':
                    start = i,j
                elif grid[i][j] == 'B':
                    box = i,j
        
        grid[start[0]][start[1]] = '.'
        grid[box[0]][box[1]] = '.'
        directions = [[-1,0], [1,0], [0,1],[0,-1]]
        q = deque()
        q.append((0, start[0], start[1], box[0], box[1]))
        seen = {}
        res = float('inf')
        while q:
            
            for i in range(len(q)):
                
                moves, s1,s2,b1,b2 = q.popleft()
                
                if (s1,s2,b1,b2) in seen and seen[(s1,s2,b1,b2)] <= moves:
                    continue
                
                seen[(s1,s2,b1,b2)] = moves
                
                if grid[b1][b2] == 'T':
                    res = min(res, moves)
                    continue
                
                for x,y in directions:
                    
                    newx, newy = s1 + x, s2 + y
                    
                    if [newx,newy] == [b1,b2]:
                        
                        #cant push box
                        if oob(b1+x,b2 + y) or (grid[b1 + x][b2 + y] != '.' and grid[b1 + x][b2 + y] != 'T'):
                            continue
                        
                        q.append((moves + 1, newx, newy, b1 + x, b2 + y))
                    elif not oob(newx,newy) and grid[newx][newy] != '#':
                        q.append((moves, newx,newy, b1,b2))
        
        return res if res != float('inf') else -1
                        
                    
                
                    