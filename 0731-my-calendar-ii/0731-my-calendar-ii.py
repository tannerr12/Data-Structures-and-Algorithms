from sortedcontainers import SortedList
class MyCalendarTwo:

    def __init__(self):
        self.h = SortedList()
        

    def book(self, start: int, end: int) -> bool:
        
        st = self.h.copy()
        st.add([start, 1])
        st.add([end,-1])
        s = 0
        
        for key,val in st:
            
            s+=val # +1 if we meet an event 
            
            if s >= 3:
                return False
            
        
        self.h.add([start,1])
        self.h.add([end,-1])
        
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)