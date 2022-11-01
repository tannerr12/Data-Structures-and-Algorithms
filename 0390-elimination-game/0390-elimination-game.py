class Solution:
    def lastRemaining(self, n: int) -> int:
        
        if n == 1:
            return 1
     
        head = 1
        remain = n
        left = True
        step = 1
        
        while remain > 1:

            if left or remain % 2 == 1:
                head += step
            
            remain = remain // 2
            step *= 2
            left = not left
        
        
        
 
        return head
                    
            
            