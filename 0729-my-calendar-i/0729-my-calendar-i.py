"""
class segTree:
    leftmost, rightmost = None,None
    segTree lChild,rChild
    s = 0
    
    def __init__(self, leftmost,rightmost,a):
        self.leftmost = leftmost
        self.rightmost = rightmost
        
        if leftmost == rightmost:
            s = a[leftmost]
        
        else:
            mid = (leftmost + rightmost) //2
            lChild = segTree(leftmost,mid,a)
            rChild = segTree(mid + 1, rightmost, a)
            recalc()
    
    
    def reclac():
        if leftmost == rightmost:
            return
        
        s = lChild.s + rChild.s
        
        
    def pointUpdate(index, newVal):
        if (leftmost == rightmost):
            s = newVal
            return
        if index <= lChild.rightmost:
            lChild.pointUpdate(index,newVal)
        else:
            rChild.pointUpdate(index,newVal)
        
        recalc()
        """
from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.arr = SortedList()

    def book(self, start: int, end: int) -> bool:
        
        res, val = self.binarySearch(start,end)
    
        if res:
            self.arr.add([start,end])
            
            return res
        else:
            return res
        
        
        
    
    def binarySearch(self, start,end):
        
        l = 0
        r = len(self.arr) -1
        
        while l <= r:
            
            curr = (l+r)//2
            s,e = self.arr[curr][0], self.arr[curr][1]
            if (s <= start and end <= e) or (end >= e and start < e) or (start <= s and end > s):
                return (False, None)
            elif start > s:
                l = curr +1
            else:
                r = curr -1
        
        
        return (True,l)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)