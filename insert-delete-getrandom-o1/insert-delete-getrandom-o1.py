class RandomizedSet:

    def __init__(self):
        self.s = {}
        self.res = []
        #self.s = set()

    def insert(self, val: int) -> bool:
        #self.arr.append(val)
        if val not in self.s:
            self.s[val] = len(self.res)
            self.res.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        
        if val in self.s:
            
            last, idx = self.res[-1], self.s[val]
            self.res[idx],self.s[last] = last,idx
            self.res.pop()
            del self.s[val]
            return True
        return False

    def getRandom(self) -> int:
        
        rand = random.randint(0, len(self.res) -1)
        
        return self.res[rand]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()