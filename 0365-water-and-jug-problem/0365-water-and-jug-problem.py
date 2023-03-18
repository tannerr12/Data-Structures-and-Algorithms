class Solution:
    def canMeasureWater(self, j1: int, j2: int, target: int) -> bool:
        
        
        p = gcd(j1,j2)
        
        return target % p == 0 and j1 + j2 >= target
        
        
        
        
        