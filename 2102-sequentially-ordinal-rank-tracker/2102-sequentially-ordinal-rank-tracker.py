class MinHeapItem:
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def __lt__(self, other):
		return self.score < other.score or \
			   (self.score == other.score and self.name > other.name)

class MaxHeapItem:
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def __lt__(self, other):
		return self.score > other.score or \
			   (self.score == other.score and self.name < other.name)

class SORTracker:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.k = 0
    def add(self, name: str, score: int) -> None:
        
        heappush(self.minheap, MinHeapItem(name, score))
      
        if len(self.minheap) > self.k + 1:
            temp = heappop(self.minheap)
            heappush(self.maxheap,MaxHeapItem(temp.name,temp.score))
        

    def get(self) -> str:
        
        res = self.minheap[0].name
        self.k +=1
        if self.maxheap:
            v = heappop(self.maxheap)
            heappush(self.minheap, MinHeapItem(v.name,v.score))
            
        return res
        
        
    

# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()