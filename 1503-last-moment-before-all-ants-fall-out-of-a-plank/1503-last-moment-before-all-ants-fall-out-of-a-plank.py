class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        
        res = 0
        for v in left:
            res = max(res, abs(0 - v))
        
        for v in right:
            res = max(res, abs(n - v))
            
    
        
        return res
        