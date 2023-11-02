class Solution:
    def minimumBoxes(self, m: int) -> int:
        cur, n1,n2 = 0,0,0
        
        while cur + (n1 +1) * (n1 + 2) // 2 <= m:
            cur += (n1 + 1) * (n1 + 2) // 2
            n1 += 1
            
            
        
        while cur < m:
            n2 += 1
            cur += n2
            
        

        return ((n1) * (n1 + 1) // 2) + n2
    
        