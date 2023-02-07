from sortedcontainers import SortedList
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        sl = SortedList(people)
        boats = 0
        boat = limit
        l = 0
        seen = set()
        while sl:
            boat -= sl[-1]
            sl.pop()
            idx = bisect.bisect_left(sl,boat)
            if idx >= len(sl) or idx != 0 and sl[idx] > boat:
                idx -=1
            
            if sl and sl[idx] <= boat:
                sl.pop(idx)
            
            boats +=1
            boat = limit
            
        return boats
            