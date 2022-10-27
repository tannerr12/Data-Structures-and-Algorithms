class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        
        p = set()
       
        val = 0
        while val ** 2  <= c:
            
            p.add(val ** 2)
            val+=1
            
        

        
        
        
        for v in p:

            if  c - v in p:
                return True
        
        return False