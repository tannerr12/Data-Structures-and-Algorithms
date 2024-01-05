class node:
    
    def __init__(self,val):
        self.next = None
        self.prev = None
        self.val = val
        
class FrontMiddleBackQueue:
    
    def __init__(self):
        self.front = node(-1)
        self.back = node(-1)
        self.front.next = self.back
        self.back.prev = self.front
        self.middle = self.front
        self.size = 0
        self.mpos = 0
    
    def updateMiddle(self, val):
        
        while self.mpos < val:
            self.middle = self.middle.next
            self.mpos += 1
        while self.mpos > val:
            self.middle = self.middle.prev
            self.mpos -=1
        
        #print(self.middle.val)
        #print(self.middle.next.val)
        #print(self.middle.prev.val)
        
    def pushFront(self, val: int) -> None:
        n = node(val)
        n.prev = self.front
        n.next = self.front.next
        self.front.next.prev = n
        self.front.next = n
        self.size += 1
        if self.middle != self.front:
            self.mpos += 1
        #where should middle be
        need = self.size // 2
        self.updateMiddle(need)
            

    def pushMiddle(self, val: int) -> None:
        n = node(val)
        #print(self.middle.val)
        #print(self.middle.next.val)
        n.prev = self.middle
        n.next = self.middle.next
        self.middle.next.prev = n
        self.middle.next = n
        self.size += 1
        #where should middle be
        need = self.size // 2
        self.updateMiddle(need)
            
    def pushBack(self, val: int) -> None:
        n = node(val)
        n.prev = self.back.prev
        n.next = self.back
        self.back.prev.next = n
        self.back.prev = n
        self.size += 1
        #where should middle be
        need = self.size // 2
        self.updateMiddle(need)

    def popFront(self) -> int:
        if self.size == 0:
            return -1

        v = self.front.next.val
        #where should middle be
        if self.middle == self.front.next:
            self.middle = self.front
            self.mpos -= 1
            
        self.front.next = self.front.next.next
        self.front.next.prev = self.front
        self.size -= 1

        if self.middle != self.front:
            self.mpos -= 1
            
        need = self.size // 2
        self.updateMiddle(need)
        return v
    def popMiddle(self) -> int:
        if self.size == 0:
            return -1
        v = 0
        #print(self.middle.val)
        #print(self.middle.next.val)
        #print(self.middle.next.next.val)
        #print(self.middle.prev.val)
        if self.size % 2 == 1:
            v = self.middle.next.val
            self.middle.next = self.middle.next.next
            self.middle.next.prev = self.middle
        else:
            v = self.middle.val
            self.middle.prev.next = self.middle.next
            self.middle.next.prev = self.middle.prev
            self.middle = self.middle.prev
            self.mpos -= 1
        self.size -= 1
        #where should middle be
        need = self.size // 2
        self.updateMiddle(need)
        return v
    def popBack(self) -> int:
        if self.size == 0:
            return -1
        v = self.back.prev.val
        if self.middle == self.back.prev:
            self.middle = self.back.prev.prev
            self.mpos -= 1
        self.back.prev = self.back.prev.prev
        self.back.prev.next = self.back
        self.size -= 1
        #where should middle be
        need = self.size // 2
        self.updateMiddle(need)
        return v
        
# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()