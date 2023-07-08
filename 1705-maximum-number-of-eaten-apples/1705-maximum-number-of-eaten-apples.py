class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        
        
        heap = []
        res = 0
        for i in range(len(apples)):
            
            if apples[i] > 0:
                heappush(heap, (i+days[i], apples[i]))
            
            while heap and heap[0][0] <= i:
                heappop(heap)
                
            if heap:
                da, app = heappop(heap)
                res += 1
                
                app -=1
                if app > 0:
                    heappush(heap, (da, app))
                    
        
        day = len(apples)
        while heap:
            
            while heap and heap[0][0] < i:
                heappop(heap)
            
            if heap:
                da, app = heappop(heap)
                res += min(app, da - day)
                day = min(day + app, day + (da - day))
                
        
        return res
                
            
            
                
                
            