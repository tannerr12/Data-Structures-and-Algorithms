class StockPrice:

    def __init__(self):
        self.mxtstamp = 0
        self.curr = 0
        self.time = {}
        self.mn = []
        self.mx = []
        self.counter = 0
        self.tombstone = defaultdict(set)

    def update(self, timestamp: int, price: int) -> None:
        if timestamp >= self.mxtstamp:
            self.curr = price
            self.mxtstamp = timestamp
        if timestamp in self.time:
            self.tombstone[self.time[timestamp][0]].add(self.time[timestamp][1])
        self.time[timestamp] = [price, self.counter]
        
        heappush(self.mn, [price, self.counter])
        heappush(self.mx, [-price, self.counter])
        self.counter +=1

    def current(self) -> int:
        return self.curr

    def maximum(self) -> int:
        while self.mx:
            val,count = self.mx[0]
            val = -val
            if val in self.tombstone and count in self.tombstone[val]:
                heappop(self.mx)
            else:
                return val
            

    def minimum(self) -> int:
        while self.mn:
            val,count = self.mn[0]
            if val in self.tombstone and count in self.tombstone[val]:
                heappop(self.mn)
            else:
                return val
            


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()