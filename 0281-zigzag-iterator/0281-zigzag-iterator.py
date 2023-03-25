class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        
        self.v1 = v1
        self.v2 = v2
        self.turn = 0
        self.i1 = 0 
        self.i2 = 0
        

    def next(self) -> int:
        if not self.hasNext():
            return None
        val = float('-inf')
        if self.turn and self.i2 < len(self.v2):
            val = self.v2[self.i2]
            self.i2 +=1
            self.turn = not self.turn
        elif not self.turn and self.i1 < len(self.v1):
            val = self.v1[self.i1]
            self.i1 +=1
            self.turn = not self.turn
        
        if self.turn and val == float('-inf'):
            val = self.v1[self.i1]
            self.i1 +=1
            self.turn = not self.turn
        elif not self.turn and val == float('-inf'):
            val = self.v2[self.i2]
            self.i2 +=1
            self.turn = not self.turn
        
        return val

    def hasNext(self) -> bool:
        if self.i1 < len(self.v1) or self.i2 < len(self.v2):
            return True
        return False
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())