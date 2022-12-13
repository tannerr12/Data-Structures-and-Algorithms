class SmallestInfiniteSet:

    def __init__(self):
        self.s = [i for i in range(1,1001)]
        self.heap = self.s.copy()
        heapq.heapify(self.heap)
        self.s = set(self.s)

    def popSmallest(self) -> int:
        if len(self.heap) == 0:
            return -1
        val = heappop(self.heap)
        self.s.remove(val)
        return val

    def addBack(self, num: int) -> None:
        if num in self.s:
            return
        
        self.s.add(num)
        heappush(self.heap,num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)