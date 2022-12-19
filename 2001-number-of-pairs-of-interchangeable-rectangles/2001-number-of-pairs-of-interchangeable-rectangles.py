class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        h = defaultdict(int)
        
        
        for i in range(len(rectangles)):
            
            x,y = rectangles[i]
            
            val = x/y
            
            h[val] +=1
        
        
    
        
        res = 0
        for key,val in h.items():
            if val > 1:
                res += ((val -1) * (val)) // 2
        
        
        return res
                
            
            