class Solution:
    def minOperations(self, n: int) -> int:
        # The idea here is we can either remove all 1 bits individually which would look like 101010101 where the bits cannot be grouped together 
        # or we can group the bits together than remove them by removing 1 bit such as 110111  -> 111000 since we add 1 to the bits which flips them all over 
        # than 111000 - > 1000000 as we do the same thing again
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