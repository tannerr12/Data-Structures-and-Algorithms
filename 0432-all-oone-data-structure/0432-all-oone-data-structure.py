class AllOne:

    def __init__(self):
        self.mp = defaultdict(int)
        

    def inc(self, key: str) -> None:
        self.mp[key] += 1

    def dec(self, key: str) -> None:
        self.mp[key] -= 1
        if self.mp[key] == 0:
            del self.mp[key]

    def getMaxKey(self) -> str:
        res,total = '',0
        for key,val in self.mp.items():
            
            if val > total:
                total = val
                res = key
        
        return res
            

    def getMinKey(self) -> str:
        res,total = '',float('inf')
        for key,val in self.mp.items():
            
            if val < total:
                total = val
                res = key
        
        return res
            


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()