class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        
        cur = 0
        res = 0
        
        for val in rungs:
            
            d = (val - cur -1) // dist
        
            res += d
            cur = val
        
        return res