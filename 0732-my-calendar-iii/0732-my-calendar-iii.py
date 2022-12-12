from sortedcontainers import SortedList
class MyCalendarThree:

    def __init__(self):
        self.arr = SortedList()

    def book(self, startTime: int, endTime: int) -> int:
        
        
        self.arr.add([startTime,1])
        self.arr.add([endTime,-1])
        s = 0
        mx = 0
        for time, val in self.arr:    
            s += val
            mx = max(mx,s)
        
        return mx
    
        
            


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)