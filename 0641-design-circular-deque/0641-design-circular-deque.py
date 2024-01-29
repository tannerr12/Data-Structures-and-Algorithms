class node:
    
    def __init__(self,val):
        
        self.next = None
        self.prev = None
        self.val = val

class MyCircularDeque:

    def __init__(self, k: int):
        self.front = node(-1)
        self.back = node(-1)
        
        self.front.next = self.back
        self.back.prev = self.front
        
        self.size = k
        self.mx = k        
    def insertFront(self, value: int) -> bool:
        if self.size == 0:
            return False
        
        nxt = self.front.next
        new = node(value)
        self.front.next = new
        nxt.prev = new
        new.prev = self.front
        new.next = nxt
        
        self.size -= 1
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.size == 0:
            return False
        
        nxt = self.back.prev
        new = node(value)
        self.back.prev = new
        nxt.next = new
        new.next = self.back
        new.prev = nxt
        self.size -= 1
        return True
        
    def deleteFront(self) -> bool:
        if self.size == self.mx:
            return False
        
        nxt = self.front.next.next
        nxt.prev = self.front
        self.front.next = nxt
        self.size += 1
        return True
    def deleteLast(self) -> bool:
        if self.size == self.mx:
            return False
        nxt = self.back.prev.prev
        nxt.next = self.back
        self.back.prev = nxt
        self.size += 1
        return True
    
    def getFront(self) -> int:
        if self.size == self.mx:
            return -1
        
        return self.front.next.val

    def getRear(self) -> int:
        if self.size == self.mx:
            return -1
        
        return self.back.prev.val

    def isEmpty(self) -> bool:
        return self.size == self.mx

    def isFull(self) -> bool:
        return self.size == 0


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()