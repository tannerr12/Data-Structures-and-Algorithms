class NumberContainers:

    def __init__(self):
        self.mp = defaultdict(int)
        self.mpOrd = defaultdict(list)
        self.tombstone = defaultdict(dict)
    def change(self, index: int, number: int) -> None:
        
        if index in self.mp:
            self.tombstone[self.mp[index]][index] = False
        
        self.mp[index] = number
        
        heappush(self.mpOrd[number], index)
        
        if number in self.tombstone and index in self.tombstone[number] and self.tombstone[number][index] == False:
            del self.tombstone[number][index]
        

    def find(self, number: int) -> int:
        #find next index
        if number in self.mpOrd:

            while self.mpOrd[number]:
                val = self.mpOrd[number][0]
                
                if number in self.tombstone and val in self.tombstone[number]:
                    heappop(self.mpOrd[number])
                else:
                    return val
            
            return -1
            
        else:
            return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)