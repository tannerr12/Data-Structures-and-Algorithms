class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
       

        for i in range(16,-1,-1):
            
            if n >= 3 ** i:
                n -= 3 ** i
        
        return n == 0