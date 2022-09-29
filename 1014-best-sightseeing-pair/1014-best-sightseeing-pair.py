class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
    
        mx = 0
        currMx = 0
        
        for i in range(len(values)):
            
            mx = max(mx,currMx + values[i])
            currMx = max(values[i],currMx) -1
        
        return mx