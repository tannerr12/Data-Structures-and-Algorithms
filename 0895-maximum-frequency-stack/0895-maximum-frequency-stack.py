class FreqStack:

    def __init__(self):
        self.heap = []
        self.h = defaultdict(int)
        self.idx = 0
    def push(self, val: int) -> None:
        
        self.h[val] +=1
        heappush(self.heap,[-self.h[val], -self.idx, val])
        self.idx +=1
        

    def pop(self) -> int:
        
        x,y,z = heappop(self.heap)
        self.h[z] -=1
        return z


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()