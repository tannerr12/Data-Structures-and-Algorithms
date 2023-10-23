class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False        

        #4 = 100
        #16 = 10000
        #64 = 1000000
        #256 =100000000
        bitCount = 0
        seen = False
        
        for i in range(32):
            if n & (1 << i) > 0:
                bitCount += 1
                if i % 2 == 0:
                    seen = True
            
        
        return bitCount == 1 and seen
            