class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        
        orig = Counter(f)
        
        for i in range(len(f)):
            
            if i == 0:
                
                if i + 1 < len(f) and f[i+1] != 1:
                    f[i] = 1 
                
                if i + 1 == len(f):
                    f[i] = 1
            
            else:
                
                if i + 1 < len(f) and f[i+1] != 1 and f[i-1] != 1: 
                    f[i] = 1 
                
                if i + 1 == len(f) and f[i-1] != 1:
                    f[i] = 1
        
        
        c = Counter(f)
        
        return c[1] - orig[1] >= n