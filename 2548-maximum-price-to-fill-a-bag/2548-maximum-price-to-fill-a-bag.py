class Solution:
    def maxPrice(self, items: List[List[int]], capacity: int) -> float:
        
        heap = []
        
        for x,y in items:
            
            r = x/y
            heappush(heap,[-r,x,y])
        
        
        res = 0
        while heap and capacity:
            
            x,y,z = heappop(heap)
            
            if z <= capacity:
                res += y
                capacity -= z
            
            else:
                rat = capacity / z
                
                res += y * rat
                capacity = 0
        
        
        return res if capacity == 0 else -1
            