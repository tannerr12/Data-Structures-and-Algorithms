class Node:
    
    def __init__(self, n):
        
        
        self.idx = n
        self.val = n
        self.nxt = None
        self.prev = None


class MRUQueue:

    def __init__(self, n: int):
        self.dhead = Node(0)
        
        self.prev = self.dhead
        self.dTail = Node(n+1)
        
        for i in range(1,n+1):
            node = Node(i)
            node.prev = self.prev
            self.prev.nxt = node
            self.prev = self.prev.nxt
            
        
        self.prev.nxt = self.dTail
        self.dTail.prev = self.prev
  
        

    def fetch(self, k: int) -> int:
        
        temp = self.dhead
        count = 0
        while temp:
            
            if count == k:
                break
            temp = temp.nxt
            count+=1
            
        
        temp.prev.nxt = temp.nxt
        temp.nxt.prev = temp.prev
        temp.prev = self.dTail.prev
        temp.nxt = self.dTail
        self.dTail.prev.nxt = temp
        self.dTail.prev = temp
        
        return temp.val
        

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)