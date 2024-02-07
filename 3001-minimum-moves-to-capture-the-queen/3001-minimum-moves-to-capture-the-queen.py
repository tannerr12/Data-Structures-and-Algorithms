class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        
        #can the rook see the queen with direct line of site?
        #can the bishop see the queen with direct line of site?
        
        #if both of these are no return 2 else return 1
        
        
        #check rook
        rookShare = False
        bishShare = False
        bishBlock = False
        
        if a == e or b == f:
            rookShare = True
        
        #same row and blocking left/right
        if a == c and a == e and f > d and f > b and d > b:
            bishBlock = True
        elif a == c and a == e and f < d and f < b and d < b:
            bishBlock = True
        
        
        #same row and blocking up and down
        elif b == d and b == f and e > a and e > c and c > a:
            bishBlock = True
            
        elif b == d and b == f and e < a and e < c and c < a:
            bishBlock = True
            
        
        #check if bishop has los on the queen
        directions = [[-1,-1], [1,1], [-1,1], [1, -1]]
        
        
        def oob(x,y):
            if x < 0 or x > 8 or y < 0 or y > 8:
                return True
            return False
        
        for x,y in directions:
            nx,ny = c,d
            while not oob(nx,ny):
                nx += x
                ny += y
                
                if (nx,ny) == (a,b):
                    break
                elif (nx, ny) == (e,f):
                    return 1
                
                
        
        if rookShare and not bishBlock:
            return 1
        return 2