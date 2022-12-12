from sortedcontainers import SortedList
class MyCalendarTwo:

    def __init__(self):
        self.arr = []
        self.double = SortedList()
    def book(self, start: int, end: int) -> bool:
        #print(self.double)
        res = self.binSearchDouble(start,end)
        if not res:
            return False
        l = self.binSearch(start,end)
        
        for i in range(len(self.arr)):
            s,e = self.arr[i]
            #double overlap
            if (start >= s and end <= e):
                self.double.add([start,end])
                
            #full overlap
            elif (start <= s and end >= e):
                self.double.add([s,e])
            
            #end overlap
            elif (start < s and e > end and s < end):
                 self.double.add([s,end])
            
            #start overlap
            elif (start > s and start < e and end > e):
                self.double.add([start,e])
        
        #print(self.double)
        self.arr.insert(l,[start,end])
        return True
        
        
            
    
    def binSearchDouble(self,start,end):
        
        l= 0
        r = len(self.double)-1
        
        while l<=r:
            
            curr = (l+r)//2
            s, e = self.double[curr]
            if (start >= s and end <= e) or (start <= s and end >= e) or (start < s and e > end and s < end) or (start > s and start < e and end > e):
                return False
            
            elif s < start:
                l = curr +1
            else:
                r = curr -1
            
        return True

        
    
    def binSearch(self,start,end):
        
        l= 0
        r = len(self.arr)-1
        
        while l<=r:
            
            curr = (l+r)//2
            s, e = self.arr[curr]
            if start >= s:
                l = curr +1
            else:
                r = curr -1
            
        return l


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)