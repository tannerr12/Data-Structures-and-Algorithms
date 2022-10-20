class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        
        
        l,r = 0,(num // 2) +1
        
        
        while l <= r:
            
            
            curr = (l+r) //2 
            
            
            if curr * curr == num:
                return True
            
            elif curr * curr > num:
                r = curr -1
                
            else:
                
                l= curr + 1
                
        
        
        
        
        return False
                