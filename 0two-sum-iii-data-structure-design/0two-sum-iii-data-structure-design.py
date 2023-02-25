class TwoSum:

    def __init__(self):
        self.nums = defaultdict(int)

    def add(self, number: int) -> None:
        self.nums[number] +=1

    def find(self, value: int) -> bool:
      
        for val in self.nums:
            if value - val in self.nums:

                if value - val == val and self.nums[val] == 1:
                    continue
                return True
                
        
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)