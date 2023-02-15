
        

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
  
        z,o = defaultdict(int), defaultdict(int)
    
        
        for i in range(len(s)-1,-1,-1):
            for j in range(len(t) -1, -1, -1):
                
                if s[i] == t[j]:
                    z[i,j] = 1 + z[i+1,j+1]
                    o[i,j] = o[i+1,j+1]
                else:
                    o[i,j] = 1 + z[i+1,j+1]
        
        
        return sum(o.values())
                    
        