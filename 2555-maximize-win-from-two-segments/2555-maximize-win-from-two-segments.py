class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        maxWin = [0] * n  
    
    
        
        for i,v in enumerate(prizePositions):
            
            idx = bisect_right(prizePositions, v + k)
            
            maxWin[i] = idx - i
            
        
        for i in range(len(prizePositions)-2,-1,-1):
        
            maxWin[i] = max(maxWin[i], maxWin[i+1])
            
        
        res = 0
        for i,v in enumerate(prizePositions):
            
            idx = bisect_right(prizePositions, v + k)
            if idx >= n:
                res = max(res,idx - i)
            else:
                res = max(res, (idx - i) + maxWin[idx])
        
        
        return res
            