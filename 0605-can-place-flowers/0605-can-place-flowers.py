class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        
      
        new = 0
        i = 0
        while i < len(f):
            if f[i] == 1:
                i += 2
                continue
            if i == 0:
                if f[i] == 0 and i + 1 < len(f) and f[i+1] != 1 or f[i] == 0 and i + 1 == len(f):
                    new +=1
                    f[i] = 1
                    i+=1
            else:
                if f[i] == 0 and i + 1 < len(f) and f[i+1] != 1 and f[i-1] != 1 or f[i] == 0 and i + 1 == len(f) and f[i-1] != 1: 
                    new +=1
                    f[i] = 1
                    i+=1
            i+=1

        return new >= n