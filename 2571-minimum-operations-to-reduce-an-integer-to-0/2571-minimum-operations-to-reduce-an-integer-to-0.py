class Solution:
    def minOperations(self, n: int) -> int:
        # The idea here is we can either remove all 1 bits individually or we can 
        count = 0
        while n:
            
            i = 0
            while i < 32:
                tcount = 0
                while i < 32 and n & (1 << i) > 0:
                    n ^= (1 << i)
                    tcount +=1
                    i+=1
                
                if tcount > 1:
                    n |= (1 << i)
                    count +=1
                elif tcount == 1:
                    count +=1
                    i+=1
                else:
                    i+=1
                
                    
        
        
       
        return count