from sortedcontainers import SortedList

class ExamRoom:

    def __init__(self, n: int):
        self.heap = []
        self.n = n
        self.sl = SortedList()
        self.seats = set()

    def seat(self) -> int:
        if len(self.heap) == 0:
            heappush(self.heap, (0,self.n-1))
            self.sl.add(0)
            self.seats.add(0)
            return 0
       # print(self.sl)
        #print(self.heap)
        v,idx = heappop(self.heap)
        #check its left and right
        
        while self.heap and idx in self.seats:
            v,idx = heappop(self.heap)
        
        
        find = bisect_left(self.sl, idx)
        vv = -v
        if find <= len(self.sl)-1:
            vv = min(abs(idx - self.sl[find]),abs(idx - self.sl[find-1]))
        else:
            vv = abs(idx - self.sl[find-1])
        
        while self.heap and ((vv < -self.heap[0][0]) or (self.heap[0][1] < idx and -self.heap[0][0] == vv) or idx in self.seats):
            v,idx = heappop(self.heap)
            find = bisect_left(self.sl, idx)
            vv = -v
            if find <= len(self.sl)-1:
                vv = min(abs(idx - self.sl[find]),abs(idx - self.sl[find-1]))
            else:
                vv = abs(idx - self.sl[find-1])
        
        #check left and right
        self.sl.add(idx)
        find = bisect_left(self.sl, idx)
        #find = bisect_left(self.sl, idx)
        
        if find != 0:
            v2 = (idx + self.sl[find-1]) //2
            left,right = self.sl[find-1], idx
            val = min(abs(left - v2), abs(right - v2))
            heappush(self.heap, (-val, v2))
        if find != len(self.sl) -1:
            v2 = (idx + self.sl[find+1]) //2
            left,right = idx, self.sl[find+1]
            val = min(abs(left - v2), abs(right - v2))
            heappush(self.heap, (-val, v2))
        
        self.seats.add(idx)
        #print(self.sl)
        return idx
        
            

    def leave(self, p: int) -> None:
        find = bisect_left(self.sl, p)
        v = 0
        #print(self.sl)
        if len(self.sl) == 1:
            self.sl.pop(find)
            self.heap = []
            self.seats.remove(p)
            return
        if find == 0:
            idx = 0
            v = self.sl[find+1]
        if find == len(self.sl) -1:
            idx = self.n-1
            v = self.n-1 - self.sl[find-1]
        
        if find > 0 and find < len(self.sl) -1:
            left, right = self.sl[find-1], self.sl[find+1]
            idx = (left + right) // 2
            v = max(idx - left, right - idx)
        heappush(self.heap, (-v,idx))
        self.sl.pop(find)
        self.seats.remove(p)
        #print(self.sl)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)