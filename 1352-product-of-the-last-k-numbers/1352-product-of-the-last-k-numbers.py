class ProductOfNumbers:

    def __init__(self):
        self.s = []
        self.s.append(1)
        self.dead = -1
        

    def add(self, num: int) -> None:
        #print(self.s)
        if len(self.s) == self.dead or num == 0:
            self.s.append(num)
            if num == 0:
                self.dead = len(self.s)
        else:
            self.s.append(num * self.s[-1])

    def getProduct(self, k: int) -> int:
        #print(self.s)
        if len(self.s) - k < self.dead:
            return 0
        else:
            if self.s[-(k+1)] > 0:
                return self.s[-1] // self.s[-(k+1)]
            else:
                return self.s[-1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)