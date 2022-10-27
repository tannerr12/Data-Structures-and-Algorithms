class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        
        p = []
       
        val = 0
        while val ** 2  <= c:
            
            p.append(val ** 2)
            val+=1
            
        
        ps = set(p)
        #print(p)
        
        
        for i in range(len(p)):
            
            
            if  c - p[i] in ps:
                return True
        
        return False