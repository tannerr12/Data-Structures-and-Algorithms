class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        res = 0
        for i,(x,y) in enumerate(classes):
            if x == y:
                res += 1
                continue
            heappush(heap,[-((x+1)/(y+1) - x/y), x, y])
        
        

        while extraStudents and heap:
            
            v, x,y = heappop(heap)
            x += 1 
            y += 1
            extraStudents -= 1
           
            
            heappush(heap, [-((x+1)/(y+1) - x/y),x,y])
        
        
        while heap:
            
            a,x,y = heappop(heap)
            
            res += x/y
        
        return res / len(classes)
            
            
            
            
            
            