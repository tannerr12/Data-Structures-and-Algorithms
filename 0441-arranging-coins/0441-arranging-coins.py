class Solution:
    def arrangeCoins(self, n: int) -> int:
            
    
        
        l,r = 0, n
        
        
        while l <= r:
            
            curr = (l+r) // 2
            
            val = curr * (curr + 1) / 2
            prev = (curr -1) * ((curr -1) + 1) / 2
            if val == n:
                return curr
            elif val > n and prev <= n:
                return curr -1
            
            elif val > n:
                r = curr -1
            
            else:
                l = curr +1
                
        
        
        return l