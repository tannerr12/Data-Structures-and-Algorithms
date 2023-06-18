class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        keyCount = 0
        start = [0,0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j].islower():
                    keyCount += 1
                if grid[i][j] == '@':
                    start = [i,j]
                
        
        directions = [[-1,0], [1,0], [0,1],[0,-1]]
        memo = set()
        
        q = deque([[start[1], start[0], 0]])
        level = 0
        while q:
            for i in range(len(q)):
                x,y,mask = q.popleft()
                
                if mask == 2 ** keyCount -1:
                    return level
                
                if (x,y,mask) in memo:
                    continue
                memo.add((x,y,mask))
                for i,j in directions:
                    newx,newy = x + i, y + j
                    if newx >= 0 and newx < len(grid[0]) and newy >= 0 and newy < len(grid) and grid[newy][newx] != '#' and (newx,newy,mask) not in memo:
                        #lock but no key
                        if (grid[newy][newx].isupper() and grid[newy][newx].isalpha() and mask & (1 << (ord(grid[newy][newx]) - ord('A'))) == 0):
                            continue
                        key = 0
                        if grid[newy][newx].islower() and grid[newy][newx].isalpha():
                            key |= (1 << (ord(grid[newy][newx]) - ord('a')))
                        
                        q.append([newx,newy,mask | key])
                        
            level +=1
            
        return -1
            
                                                                         
                