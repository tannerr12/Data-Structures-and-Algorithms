class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.arr = []
        for i in range(len(vec)):
            for j in range(len(vec[i])):
                self.arr.append(vec[i][j])
                
        self.idx = 0    

    def next(self) -> int:
        
        val = self.arr[self.idx]
        self.idx +=1
        return val
    def hasNext(self) -> bool:
        return self.idx < len(self.arr)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()