class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1 or n == 4:
            return True
        

        #4 = 100
        #16 = 10000
        #64 = 1000000
        #256 =100000000
        bitCount = 0
        seen = False
        
        for i in range(32):
            if n & (1 << i) > 0:
                bitCount += 1
            
        for i in range(2, 32, 2):
            if n & (1 << i) > 0:
                seen = True
                
        
        
        return bitCount == 1 and seen
            