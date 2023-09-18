class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        
        self.ranges = []
        blacklist.sort()
        prev = 0
        for v in blacklist:
            if v -1 >= prev:
                self.ranges.append((prev, v - 1))
                
            prev = v + 1
        
        if n -1 >= prev:
            self.ranges.append((prev, n -1))
        self.n = n
        self.ptr = self.ranges[0][0]
        self.idx = 0
        
        
    def pick(self) -> int:
        
        if self.ptr < self.ranges[self.idx][1]:
            self.ptr += 1
        
        else:
            self.idx += 1
            self.idx %= len(self.ranges)
            self.ptr = self.ranges[self.idx][0]
        
        return self.ptr


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()