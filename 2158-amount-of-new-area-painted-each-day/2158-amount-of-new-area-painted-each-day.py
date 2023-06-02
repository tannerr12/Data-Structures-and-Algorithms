from sortedcontainers import SortedList
class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        res = [0] * len(paint)
        sl = SortedList()
        for i, (x,y) in enumerate(paint):
            sl.add([x, i,0])
            sl.add([y, i,1])
        
        
        slcurrent = SortedList()
        last = -1
        for i in range(len(sl)):
            
            x,y,typ = sl[i]
            
            if slcurrent:
                res[slcurrent[0]] += x - last 
            
            if typ == 1:
                slcurrent.remove(y)
            elif typ == 0:
                slcurrent.add(y)
            
            last = x
        
        return res
            
            
            
            
            
            
            
            
            
        
        
            