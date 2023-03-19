from sortedcontainers import SortedList
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        sl = SortedList()
        
        for s,e in slots1:
            sl.add((s, 1))
            sl.add((e,-1))
        
        for s,e in slots2:
            sl.add((s, 1))
            sl.add((e,-1))
            
        
        doubleT = []
        count = 0
        s,e = float('inf'), float('-inf')
        for time, val in sl:
            if val > 0:
                count += val
            
            if count == 2:
                s = min(time, s)
                e = max(time, e)
                if e-s >= duration:
                    return [s, s + duration]
                
            if val < 0:
                count += val
            
            if count < 2:
                s,e = float('inf'), float('-inf')
            
            
        
        return []
                
            