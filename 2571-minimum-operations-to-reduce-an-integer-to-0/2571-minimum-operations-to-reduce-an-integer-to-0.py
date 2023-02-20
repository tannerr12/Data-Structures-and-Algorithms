class Solution:
    def minOperations(self, n: int) -> int:
        res = float('inf')
        count = 0
        countzero = 0
        mn = n
        tcount = 0
        for i in range(32):
            
            if mn & (1 << i) > 0:
                count +=1
                countzero += tcount
                tcount = 0
            else:
                tcount +=1

        res = min(res,count,countzero +2)
        #1, 2, 4, 8, 16, 32, 64, 128, 256, 512
        if res <= 1:
            return res
        #1, 2, 4, 8, 16, 32, 64, 128, 256, 512
        
        count = 0
        #100111
        #110110
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
                
                    
        
        
       
        return min(res,count)