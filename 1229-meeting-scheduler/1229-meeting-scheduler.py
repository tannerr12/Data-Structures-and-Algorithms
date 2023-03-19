
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        sl = []
        
        for s,e in slots1:
            sl.append((s, 1))
            sl.append((e,-1))
        
        for s,e in slots2:
            sl.append((s, 1))
            sl.append((e,-1))
            
        
        sl.sort()
        count = 0
        s = float('inf')
        for time, val in sl:
            if val > 0:
                count += val
            
            if count == 2:
                s = min(time, s)
                if time-s >= duration:
                    return [s, s + duration]
                
            if val < 0:
                count += val
            
            if count < 2:
                s = float('inf')
            
            
        
        return []
                
            