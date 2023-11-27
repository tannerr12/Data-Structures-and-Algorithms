class Solution:
    def maxArea(self, h: int, w: int, hz: List[int], vz: List[int]) -> int:
        
        MOD = 10 ** 9 + 7
        hz.append(0)
        vz.append(0)
        hz.append(h)
        vz.append(w)
        hz.sort()
        vz.sort()
        
        besth = 0
        bestv = 0
        for i in range(1,len(hz)):
            besth = max(besth, hz[i] - hz[i-1])
            
        for i in range(1, len(vz)):
            bestv = max(bestv, vz[i] - vz[i-1])
            
        
        return (besth * bestv) % MOD
        