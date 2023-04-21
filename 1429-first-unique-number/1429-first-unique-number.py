class FirstUnique:

    def __init__(self, nums: List[int]):
        self.count = defaultdict(int)
        self.q = deque()
        for val in nums:
            self.q.append(val)
            self.count[val] +=1
        

    def showFirstUnique(self) -> int:
        while self.q and self.count[self.q[0]] > 1:
            self.q.popleft()
        
        return self.q[0] if self.q else -1

    def add(self, value: int) -> None:
        if self.count[value] == 0:
            self.q.append(value)
            
        self.count[value] +=1
        while self.q and self.count[self.q[0]] > 1:
            self.q.popleft()


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)