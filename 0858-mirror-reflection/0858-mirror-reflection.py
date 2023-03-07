class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        
        
        #top left = divisible by p and bounces are even cycle odd
        #top right = divisible by p and bounces are odd cycle odd
        #bottom right = divisible by p and bounces odd and cycle even
        
        if q == p:
            return 1
        if q == 0:
            return 0
        val = q
        cycle = 1
        bounce = 1
        while val != 0:
            
            if val + q > p:
                cycle +=1
            val += q
            val %= p
            bounce +=1
            
        
        
        #print(cycle)
        #print(bounce)
        
        if cycle % 2 and bounce % 2 == 0:
            return 2
        if cycle % 2 and bounce % 2:
            return 1
        else:
            return 0