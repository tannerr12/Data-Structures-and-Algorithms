class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        
        cur = 0
        res = 0
        
        for val in rungs:
            
            d = val - cur
            
            minus = 0
            if d % dist == 0:
                minus = -1
            if d > dist:
                res += (d // dist) + minus
            cur = val
        
        return res