class Solution:
    def appealSum(self, s: str) -> int:
        
        N = len(s)
        seen = {}
        total = 0
        for i,c in enumerate(s):
            
            if c in seen:
                
                left = i - seen[c] 
                right = N - i
                
                total += left * right
            
            else:
                
                left = i + 1
                
                right = N - i
                
                total += left * right
            
            
            seen[c] = i
            
        
        
        return total