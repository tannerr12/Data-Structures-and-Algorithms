class Node:
    def __init__(self):
        self.prev = None
        self.next = None
        self.val = float('inf')
        
class MaxStack:

    def __init__(self):
        self.h = {}
        self.stack = []
        self.count = 0
        self.heap = []
        self.removed = set()
        

    def push(self, x: int) -> None:
        self.count +=1
        #print(self.count)
        self.h[self.count] = x
        heapq.heappush(self.heap, (-x,-self.count))
        

    def pop(self) -> int:
        if len(self.h) == 0:
            return 0

        val = 0

        c = self.count *1
        while c not in self.h:
            c -=1
        val = self.h[c]
        del self.h[c]
        self.removed.add(-c)
        return val
    

    def top(self) -> int:
        c = self.count
        while c not in self.h:
            c-=1
        
        
        return self.h[c]

    def peekMax(self) -> int:
      
        val,key = self.heap[0]
        while self.heap[0][1] in self.removed:
            val,key = heapq.heappop(self.heap)
        
        return self.heap[0][0] * -1

    def popMax(self) -> int:
        val,key = self.heap[0]

        while self.heap[0][1] in self.removed:
            val,key = heapq.heappop(self.heap)
        
        val, key = heapq.heappop(self.heap)
      
        del self.h[key * -1]
        self.removed.add(key)
        return val * -1


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()