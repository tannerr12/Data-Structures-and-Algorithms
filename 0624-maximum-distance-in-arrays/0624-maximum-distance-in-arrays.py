class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        mn = arrays[0][-1]
        mx = arrays[0][0]
        res = 0
        
        for i in range(len(arrays)):
            
            res = max(res, abs(arrays[i][-1] - mn), abs(arrays[i][0] - mx))
            mn = min(mn, arrays[i][0])
            mx = max(mx, arrays[i][-1])
            
    
        
        return res