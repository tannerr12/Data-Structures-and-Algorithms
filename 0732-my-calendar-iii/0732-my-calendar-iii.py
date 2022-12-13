class Tree:
    def __init__(self, low, high, val=0):
        self.low = low
        self.high = high
        self.val = val
        self.left = None
        self.right = None
        
    def push_down(self): 
        self.val += 1
        if self.left: 
            self.left.push_down()
        if self.right: 
            self.right.push_down()
    def update(self, i, j):
        if self.low == i and self.high == j:
            self.val += 1
            if self.left: 
                self.left.push_down()
            if self.right: 
                self.right.push_down()
            return self.val
        
        
        mid = (self.low + self.high) // 2
        if not self.left and not self.right:
            self.left = Tree(self.low, mid, self.val)
            self.right = Tree(mid, self.high, self.val)
        if mid <= i:
            self.val = max(self.val, self.right.update(i, j))
        elif mid >= j:
            self.val = max(self.val, self.left.update(i, j))
        else:
            l = self.left.update(i, mid)
            r = self.right.update(mid, j)
            self.val = max(self.val, max(l, r))
        return self.val



from sortedcontainers import SortedList
class MyCalendarThree:

    def __init__(self):
        self.low = 0
        self.high = 10 ** 9
        self.tree = Tree(self.low, self.high)

    def book(self, x: int, y: int) -> int:
        return self.tree.update(x, y)






        
            


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)