class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        res = 0
        l = 0
        last = -1
        count = defaultdict(int)
        
        
        for i in range(len(s)):
            
            count[s[i]] += 1            
               
            while count[s[i]] > 1:
                
                count[s[l]] -= 1
                l += 1
            
            
            res += i - l + 1
        
     
    
        
        return res 
            
            