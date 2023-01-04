class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        h = Counter(s)
        if len(h.keys()) != 3:
            return -1
        c = {}
        for key,val in h.items():
            
            h[key] -= k
            
            if h[key] < 0:
                return -1
            
            c[key] = 0
        res = float('inf')
        l = 0
        
        
        for i in range(len(s)):
            w = s[i]
            c[w] +=1
            
            while c[w] > h[w]:
                c[s[l]] -=1
                l+=1
            
            res = min(res, l + len(s) - i -1)
            
        
        return res
            
            
            
            