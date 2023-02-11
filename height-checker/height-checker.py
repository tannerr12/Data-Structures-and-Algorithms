class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        h = heights.copy()
        hasSwapped = True
        
        while hasSwapped:
            hasSwapped = False
            for i in range(len(heights)-1):
                
                if heights[i+1] < heights[i]:
                    
                    heights[i+1],heights[i] = heights[i], heights[i+1]
                    hasSwapped = True
        
        
        res = 0
        for x,y in zip(heights,h):
            
            if x != y:
                res +=1
        
        return res
