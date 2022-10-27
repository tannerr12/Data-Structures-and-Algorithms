class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        
        p = []
        
        val = 0
        while val ** 2  <= c:
            
            p.append(val ** 2)
            val+=1
            
        
        
        #print(p)
        
        
        for i in range(len(p)):
            
            
            
            l,r = i,len(p) -1
            
            
            
            while l <= r:
                
                curr = (l+r) // 2
                
                if p[curr] + p[i] == c:
                    return True
                
                
                elif p[curr] + p[i] > c:
                    r = curr -1
                else:
                    l = curr +1
                    
            
        
        return False