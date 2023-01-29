class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        res = set()
        
        def countLattice(x,y,r):
            
            
            for i in range(-r, r+1):
                
                for j in range(-r, r +1):
                    
                
                    posx = x + j
                    posy = y + i
                    
                    if (x - posx) ** 2 + (y - posy) ** 2 <= r * r:
                        res.add((posx,posy))
            
            
            
        
        for x,y,z in circles:
            
            countLattice(x,y,z)
            
        
        #print(res)
        return len(res)
            
            