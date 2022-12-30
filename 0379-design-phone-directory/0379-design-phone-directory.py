class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.heap = [i for i in range(maxNumbers)]        
        self.s = set()
    def get(self) -> int:
        if not self.heap:
            return -1
        n = heappop(self.heap)
        self.s.add(n)
        return n
    def check(self, number: int) -> bool:
        return number not in self.s

    def release(self, number: int) -> None:
        if number in self.s:
            self.s.remove(number)        
            heappush(self.heap,number)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)