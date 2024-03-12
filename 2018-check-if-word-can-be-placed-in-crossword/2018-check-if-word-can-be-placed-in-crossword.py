class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        
        toCheck = set()
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        opposite = {(1,0):(-1,0), (-1,0):(1,0), (0,1):(0,-1), (0,-1):(0,1)}
        dmap = {0:[[0,1],[0,-1]], 1:[[1,0],[-1,0]]}
        def valid(x,y):
            
            if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and board[x][y] != '#':
                return True
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '#':
                    continue
                validC = 0
                d = [-1,-1]
                for x,y in directions:
                    nx,ny = i + x, j + y
                    if not valid(nx,ny):
                        toCheck.add((i,j,opposite[(x,y)][0], opposite[(x,y)][1]))
        
        #print(toCheck)
        '''
        def validPath(vert, pos, x, y):
            
            if (board[x][y] != word[pos] and board[x][y] != ' '):
                return False
            
            if vert == 1:
                for a,b in dmap[vert]:
                    if a >= 0 and b >= 0 and a < len(board[0]) and b < len(board) and board[a][b] != '#' 
                        return False
            
            return True
        '''
        for i,j,d1,d2 in toCheck:
            
            cur = 0
            
            ci,cj = i,j
            
            ci += d1 * (len(word) -1)
            cj += d2 * (len(word) -1)
            
            if (ci,cj,opposite[(d1,d2)][0], opposite[(d1,d2)][1]) not in toCheck:
                continue
            
            ci,cj = i,j
            found = True
            for _ in range(len(word)):
                
                if board[ci][cj] != ' ' and board[ci][cj] != word[cur]:
                    found = False
                    break
                cur += 1
                ci += d1
                cj += d2
            
            if found:
                return True
        
        return False
            
                    