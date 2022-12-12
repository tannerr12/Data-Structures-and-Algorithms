class Solution:
    def climbStairs(self, n: int) -> int:
       
    
        if n == 1:
            return 1
        first = 1
        second = 2
        
        
        for i in range(3, n+1):
            
            s = second
            second = first + second
            first = s
        
        
        return second
            