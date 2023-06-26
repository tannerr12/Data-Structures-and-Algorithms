class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        
        k = 0
        while num1 > 0:
            num1 -= num2
            k += 1
            if num1.bit_count() <= k <= num1:
                return k
        return -1
            
                    