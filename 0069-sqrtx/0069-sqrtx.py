class Solution:
    def mySqrt(self, x: int) -> int:
        
        
        
        l,r = 0,x
        
        
        while l <= r:
            
            curr = (l+r) //2
            
            
            if curr * curr == x or ((curr+1) * (curr+1) > x and curr * curr < x):
                return curr
            
            elif curr * curr > x:
                r = curr -1
            else:
                l = curr +1
        
        
        return 0
                