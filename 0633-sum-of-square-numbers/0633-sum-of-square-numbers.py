class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        
        p = set()
       
        val = 0
        while val ** 2  <= c:
            
            p.add(val ** 2)
            if c - val **2 in p:
                return True
            val+=1
            
        

        
