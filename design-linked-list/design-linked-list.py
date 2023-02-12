class Node:
    
    def __init__(self, val):
        
        self.val = val
        self.next = None
        self.prev = None
        

class MyLinkedList:

    def __init__(self):
        self.tail = Node(-1)
        self.head = Node(-1)
        
        self.tail.prev = self.head
        self.head.next = self.tail
        
    def p(self):
        dhead = self.head
        
        while dhead:
            print(dhead.val)
            dhead = dhead.next
        
        
    def get(self, index: int) -> int:
        #self.p()
        dhead = self.head
        
        for i in range(index +1):
            if dhead == self.tail:
                return -1
            dhead = dhead.next
        
        return dhead.val
    
    def addAtHead(self, val: int) -> None:
        n = Node(val)
        n.next = self.head.next
        self.head.next = n
        n.next.prev = n
        n.prev = self.head
        #self.p()
    def addAtTail(self, val: int) -> None:
        n = Node(val)
        n.next = self.tail
        n.prev = self.tail.prev
        self.tail.prev = n
        n.prev.next = n
        #self.p()

    def addAtIndex(self, index: int, val: int) -> None:
        dhead = self.head
        
        for i in range(index):
            if not dhead:
                return
            dhead = dhead.next
        if dhead == self.tail:
            return
        if dhead == self.head:
            self.addAtHead(val)
        elif dhead.next == self.tail:
            self.addAtTail(val)
        
        else:
            n = Node(val)
            d = dhead.next
            dhead.next.prev = n
            dhead.next = n
            n.prev = dhead
            n.next = d
        
        #self.p()
            
        
    def deleteAtIndex(self, index: int) -> None:
        #self.p()
        dhead = self.head
   
        for i in range(index):
            if not dhead:
                return
                
            dhead = dhead.next
        
        if dhead == self.head:
            if self.head.next == self.tail:
                return
            v = self.head.next
            self.head.next = self.head.next.next
            v.next.prev = self.head
            v.next = None
            v.prev = None
        elif dhead == self.tail:
            return
        else:
            v = dhead.next
            if v == self.tail:
                return
            dhead.next = dhead.next.next
            v.next.prev = dhead
            v.next = None
            v.prev = None
        #self.p()


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)