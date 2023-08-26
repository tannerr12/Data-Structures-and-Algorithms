class DoubleLinked:
    def __init__(self, key):
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
            new = DoubleLinked(key)
            new.next = self.head.next
            self.head.next.prev = new
            self.head.next = new
            new.prev = self.head
            self.mp[key] = new
        else:
            self.mp[key].count += 1
            current = self.mp[key]
            while current.next.count < current.count:
                next_node = current.next
                current.prev.next = next_node
                next_node.prev = current.prev
                current.next = next_node.next
                current.next.prev = current
                next_node.next = current
                current.prev = next_node

    def dec(self, key: str) -> None:
        if key not in self.mp: 
            return
        self.mp[key].count -= 1
        if self.mp[key].count == 0:
            prv = self.mp[key].prev
            nxt = self.mp[key].next
            prv.next = nxt
            nxt.prev = prv
            del self.mp[key]
        else:
            current = self.mp[key]
            while current.prev.count > current.count:
                prev_node = current.prev
                prev_node.next = current.next
                current.next.prev = prev_node
                current.prev = prev_node.prev
                prev_node.prev.next = current
                prev_node.prev = current
                current.next = prev_node

    def getMaxKey(self) -> str:
        return self.tail.prev.key

    def getMinKey(self) -> str:
        return self.head.next.key
