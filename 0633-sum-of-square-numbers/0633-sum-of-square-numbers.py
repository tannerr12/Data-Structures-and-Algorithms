class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        
        seen = set()
       
        val = 0
        while val ** 2  <= c:
            
            seen.add(val ** 2)
            if c - val **2 in seen:
                return True
            val+=1
            
        

        
