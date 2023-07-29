class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        def oob(i,j):
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]):
                return True
            return False
            
        def manhat(i,j):
            #manhatten distance
            return abs(i - target[0]) + abs((j - target[1]))
   
        start = 0,0
        box = 0,0
        target = 0,0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'S':
                    start = i,j
                elif grid[i][j] == 'B':
                    box = i,j
                elif grid[i][j] == 'T':
                    target = i,j
        
        grid[start[0]][start[1]] = '.'
        grid[box[0]][box[1]] = '.'
        directions = [[-1,0], [1,0], [0,1],[0,-1]]
        q = []
        q.append((manhat(box[0],box[1]),0,start[0], start[1], box[0], box[1]))
        seen = {}
        
        while q:

            _, moves, s1,s2,b1,b2 = heappop(q)

            if b1 == target[0] and b2 == target[1]:
                return moves

            if (s1,s2,b1,b2) in seen:
                continue

            seen[(s1,s2,b1,b2)] = moves

            for x,y in directions:

                newx, newy = s1 + x, s2 + y

                if [newx,newy] == [b1,b2]:

                    #cant push box
                    if oob(b1+x,b2 +y) or (grid[b1 + x][b2 + y] != '.' and grid[b1 + x][b2 + y] != 'T'):
                        continue

                    heappush(q,(manhat(b1 + x,b2 + y) + moves + 1,moves + 1, newx, newy, b1 + x, b2 + y))
                elif not oob(newx,newy) and grid[newx][newy] != '#':
                    heappush(q,(manhat(b1, b2) + moves, moves, newx,newy, b1,b2))

        return -1
                        
                    
                
                    