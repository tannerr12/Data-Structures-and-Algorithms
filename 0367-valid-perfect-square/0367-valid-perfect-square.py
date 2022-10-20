class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        
        
        i  = 1
        
        target = 1
        
        while target <= num:
            target = i * i
            
            if target == num:
                return True
            i +=1
        
        return False