class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        fracMap = set()
        res = []
        for i in range(1,n):
            frac = str(i) + '/' 
            for j in range(i + 1, n+1):
                if i / j not in fracMap:
                    res.append(frac + str(j))
                    fracMap.add(i/j)
                    
        
        
        return res
                