class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        
        l = 0
        res = 0
        h = defaultdict(int)
        
        for i in range(len(s)):
            
            h[s[i]]+=1
            
            
            while h['a'] > 0 and h['b'] > 0 and h['c'] > 0:
                
                h[s[l]] -=1
                l+=1
                
                res += 1 + (len(s) - (i + 1))
                
                
            
        return res
        