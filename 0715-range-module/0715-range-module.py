from sortedcontainers import SortedList
class RangeModule:

    def __init__(self):
        self.sl = SortedList()

    def addRange(self, left: int, right: int) -> None:
        if len(self.sl) == 0:
            self.sl.add([left,right])
            return
        
        #print(self.sl)
        lIdx = bisect_left(self.sl,left,key = lambda x: x[1])
        if lIdx >= len(self.sl) or right < self.sl[lIdx][0]:
            self.sl.add([left,right])
        #    print(self.sl)
            return
        start = min(left, self.sl[lIdx][0])
        end = right
        while self.sl and lIdx < len(self.sl) and self.sl[lIdx][0] <= right:
            end = max(right, self.sl[lIdx][1])
            self.sl.pop(lIdx)
            
        
        self.sl.add([start,end])
        #print(self.sl)
        

    def queryRange(self, left: int, right: int) -> bool:
        lIdx = bisect_left(self.sl,left,key = lambda x: x[1])
        #print(self.sl)
        if lIdx < len(self.sl) and self.sl[lIdx][0] <= left and self.sl[lIdx][1] >= right:
            return True
        return False
  
    def removeRange(self, left: int, right: int) -> None:
        lIdx = bisect_left(self.sl,left,key = lambda x: x[1])
        if lIdx >= len(self.sl) or right < self.sl[lIdx][0]:
            return 
        start = self.sl[lIdx][0]
        end = left
        e=self.sl[lIdx][1]    
        self.sl.pop(lIdx)
    
        while self.sl and lIdx < len(self.sl) and self.sl[lIdx][0] <= right:
            
            e = self.sl[lIdx][1]
            self.sl.pop(lIdx)
        
        if start < end:
            self.sl.add([start, end ])
        if right < e:
            self.sl.add([right, e])
        
        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)