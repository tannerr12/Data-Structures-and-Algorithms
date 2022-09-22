class RandomizedSet:

    def __init__(self):
        self.h = {}
        
        self.s = set()

    def insert(self, val: int) -> bool:
        #self.arr.append(val)
        if val not in self.s:
            self.s.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.s:
            self.s.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        arr = list(self.s)
        rand = random.randint(0, len(arr) -1)
        
        return arr[rand]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()