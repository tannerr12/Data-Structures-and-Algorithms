class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        heapify(buses)
        heapify(passengers)
        
        heap= []
        
        res = 0
        seen = set()
        while buses:
            
            arrival = heappop(buses)
            c = capacity
            while passengers and passengers[0] <= arrival and c:
                
                p = heappop(passengers)
                seen.add(p)
                if p -1 <= arrival and p-1 not in seen:
                    res = max(res, p-1)
                    
                    
                c -=1
            if c > 0:
                if arrival not in seen:
                    res = max(res,arrival)
        return res
        
        