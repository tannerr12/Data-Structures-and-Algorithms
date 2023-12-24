class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        rem = 0
        
        for i in range(100000):
            
            rem *= 10 
            rem += 1
            
            if rem % k == 0:
                return i + 1
            
            rem %= k
        
        return -1
    
        
        