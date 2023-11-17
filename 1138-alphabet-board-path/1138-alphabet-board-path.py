class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        manhat = defaultdict(tuple)
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                cur = board[i][j]
                manhat[cur] = (i,j)
                if cur == 'z':
                    break
        
        #print(manhat)

        res = ''
        x,y = 0,0
   
        for i in range(len(target)):
            cur = board[x][y]    
            find = target[i]
            distanceVert = x - manhat[find][0]
            distanceHor = y - manhat[find][1]
            
            x -= distanceVert
            y -= distanceHor
            
            if cur != 'z':
                if distanceHor > 0:
                    res += 'L' * distanceHor
                elif distanceHor < 0:
                    res += 'R' * abs(distanceHor)
                if distanceVert > 0:
                    res += 'U' * distanceVert
                elif distanceVert < 0:
                    res += 'D' * abs(distanceVert)
            else:
                if distanceVert > 0:
                    res += 'U' * distanceVert
                elif distanceVert < 0:
                    res += 'D' * abs(distanceVert)
                if distanceHor > 0:
                    res += 'L' * distanceHor
                elif distanceHor < 0:
                    res += 'R' * abs(distanceHor)
            
            res += '!'
          
            
        return res
            