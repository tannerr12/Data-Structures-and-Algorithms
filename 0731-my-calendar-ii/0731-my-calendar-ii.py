class MyCalendarTwo:

    def __init__(self):
        self.h = {}

    def book(self, start: int, end: int) -> bool:
        if start not in self.h:
            self.h[start] = 1
        else:
            self.h[start]+=1
        
        if end not in self.h:
            self.h[end] = -1
        else:
            self.h[end] -=1
        s = 0
        
        #print(self.h)
        for key,val in sorted(self.h.items()):
            
            s+=val # +1 if we meet an event 
            
            if s >= 3:
                
                self.h[start] -=1
                self.h[end] +=1
                return False
            
            
        
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)