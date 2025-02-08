class NumberContainers:

    def __init__(self):
        self.ind = defaultdict(int)
        self.nums = defaultdict(list)
        
        

    def change(self, index: int, number: int) -> None:
        self.ind[index] = number
        heappush(self.nums[number], index)

    def find(self, number: int) -> int:
        
        while self.nums[number]:
            val = self.nums[number][0]
            if self.ind[val] == number:
                return val
            heappop(self.nums[number])
        
        return -1
            


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)