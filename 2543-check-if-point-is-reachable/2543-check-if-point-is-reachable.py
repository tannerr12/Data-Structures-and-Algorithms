class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        
        
        def check(x):
            
            return (x  & (x - 1)) == 0
        
        
        return check(targetX) or check(targetY) or check(gcd(targetX,targetY))
   
            
            