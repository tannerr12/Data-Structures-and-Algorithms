class FirstUnique:

    def __init__(self, nums: List[int]):
        self.mp = {}
        self.deleted = set()
        for val in nums:
            self.add(val)

    def showFirstUnique(self) -> int:
        
        return next(iter(self.mp)) if self.mp else -1
    
    def add(self, value: int) -> None:
        
        if value in self.deleted:
            return
        if value in self.mp:
            del self.mp[value]
            self.deleted.add(value)
        else:
            self.mp[value] = 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)