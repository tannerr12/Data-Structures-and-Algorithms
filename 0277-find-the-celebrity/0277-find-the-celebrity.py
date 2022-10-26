# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
   
            
            
  
        
        
        cantidate = 1
        for i in range(n):
            
            if i == cantidate:
                continue
            if knows(cantidate,i):
                
                cantidate = i
        
        c= cantidate
        for i in range(n):
                
            if i == c:
                continue
               
            if knows(c,i) or not knows(i,c):
                return -1
            
            
            
        return cantidate
    
    
    
        
        

        

    
            
            