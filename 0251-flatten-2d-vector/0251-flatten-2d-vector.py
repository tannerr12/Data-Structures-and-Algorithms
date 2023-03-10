class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.i = 0
        self.j = 0    
        self.vec = vec

        while self.hasNext() and self.j == len(self.vec[self.i]):
            self.i+=1
            self.j = 0
    def next(self) -> int:
        
        val = self.vec[self.i][self.j]
        self.j +=1
        while self.hasNext() and self.j == len(self.vec[self.i]):
            self.i+=1
            self.j = 0
        return val
    def hasNext(self) -> bool:
        return self.i < len(self.vec)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()