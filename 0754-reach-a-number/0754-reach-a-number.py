class Solution:
    def reachNumber(self, target: int) -> int:
        
        target = abs(target)

        total = 0
        
        step = 1
        
        
        while True:
        
            total += step
            
            
            if total >= target and target % 2 == total % 2:
                return step
            
            
            step +=1
            
        
        
        
        
        