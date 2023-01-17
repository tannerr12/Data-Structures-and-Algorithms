class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        
   
        
        l = 0
        res = 0
        total = 0
        for i in range(len(s)):
            
            total += abs((ord(s[i]) - ord('a')) - (ord(t[i]) - ord('a')))
            
            while total > maxCost:
                
                res = max(res, (i - l))
                total -= abs((ord(s[l]) - ord('a')) - (ord(t[l]) - ord('a')))
                l+=1
        
        
        
        res = max(res, len(s) - l)
        return res
            