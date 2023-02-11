class Solution:
    def countQuadruples(self, f: str, s: str) -> int:


        c1 = Counter()
        c2 = Counter()
        
        for i in range(len(f)):
            
            if f[i] not in c1:
                c1[f[i]] = i
        
        for i in range(len(s)):
            c2[s[i]] = i
        
        
        res = 0
        dist = float('inf')
        for key,val in c1.items():
            
            if key in c2:
                
                if val - c2[key] < dist:
                    res = 1
                    dist = val - c2[key]
                elif val - c2[key] == dist:
                    res +=1
        
        
        return res
        
            