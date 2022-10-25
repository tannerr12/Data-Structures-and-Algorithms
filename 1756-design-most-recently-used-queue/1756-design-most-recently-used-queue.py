from sortedcontainers import SortedList


class MRUQueue:

 
    def __init__(self, n: int):
        self.data = SortedList((i, i) for i in range(1, n+1))

    def fetch(self, k: int) -> int:
        
        _, x = self.data.pop(k-1)
        i = self.data[-1][0] + 1 if self.data else 0
        self.data.add((i, x))
        return x


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)