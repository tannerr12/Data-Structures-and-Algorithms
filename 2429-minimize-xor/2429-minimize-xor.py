class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        count = num2.bit_count()
        x= 0
        for i in range(32,-1,-1):
            if count == 0:
                break
            if num1 & (1 << i) >0:
                x |= (1 << i)
                count -=1
            
        
        for i in range(32):
            if count ==0:
                break
            if x & (1 << i) > 0:
                continue
            x |= (1 << i)
            count -=1
        
        
        return x
            
        
        