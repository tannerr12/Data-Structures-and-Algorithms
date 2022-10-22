class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        
      
        val = 0
        i = 1
        while val <= n:
            
            val =  i * (i + 1) / 2
            
            i +=1
        
        i -=1
        if val != n:
            i-=1
        return i