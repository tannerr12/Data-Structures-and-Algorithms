class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.q = deque()
        c = 0
        for i in range(len(encoding)):
            if i % 2==0:
                c = encoding[i]
            else:
                if c == 0:
                    continue
                self.q.append([encoding[i], c])
                
        #print(self.q)
    def next(self, n: int) -> int:
        res = -1
        while self.q and n:
            if self.q[0][1] < n:
                n-= self.q[0][1]
                self.q.popleft()
            elif self.q[0][1] == n:
                res = self.q[0][0]
                self.q.popleft()
                n = 0
            else:
                self.q[0][1] -= n
                n = 0
                res = self.q[0][0]
        
        if n == 0:
            return res
        else:
            return -1
        

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)