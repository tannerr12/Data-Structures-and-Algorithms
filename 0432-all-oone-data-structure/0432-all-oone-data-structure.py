class DoubleLinked:
    
    def __init__(self,key):
        
        self.key = key
        self.count = 1
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.mp = {}
        self.head = DoubleLinked('')
        self.tail = DoubleLinked('')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.head.count = float('-inf')
        self.tail.count = float('inf')
    def inc(self, key: str) -> None:
        if key not in self.mp:
            #add a value to the tail
            
            new = DoubleLinked(key)
            new.prev = self.head
            new.next = self.head.next
            self.head.next = new
            new.next.prev = new
            self.mp[key] = new
        else:
            #increment and shift if needed
            self.mp[key].count += 1
            current = self.mp[key]
            while current.next.count < current.count:
                #swap them
                nxt = current.next
                prv = current.prev
                current.next = nxt.next
                current.prev = nxt
                current.next.prev = current
                nxt.next = current
                nxt.prev = prv
                prv.next = nxt               
      
    def dec(self, key: str) -> None:
        
        self.mp[key].count -=1
        if self.mp[key].count == 0:
            #remove
            prv = self.mp[key].prev
            nxt = self.mp[key].next
            prv.next = nxt
            nxt.prev = prv
            self.mp[key].prev = None
            self.mp[key].next = None
            
            del self.mp[key]
        else:
            current = self.mp[key]
            while current.prev.count > current.count:
                #swap them
                nxt = current.next
                prv = current.prev
                current.next = prv
                current.prev = prv.prev
                current.prev.next = current
                prv.next = nxt 
                prv.prev = current
                nxt.prev = prv               

    def getMaxKey(self) -> str:
        return self.tail.prev.key
            

    def getMinKey(self) -> str:
        return self.head.next.key
            


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()