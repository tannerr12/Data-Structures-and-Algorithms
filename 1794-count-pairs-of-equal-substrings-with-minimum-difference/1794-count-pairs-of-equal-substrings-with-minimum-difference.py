class Solution:
    def countQuadruples(self, firstString: str, secondString: str) -> int:
        f = firstString
        #s = secondString[::-1]
        s = secondString

       # l,r = 0,0
        
      #  while l < len(firstString) and r >=0:
        
        
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
        
            