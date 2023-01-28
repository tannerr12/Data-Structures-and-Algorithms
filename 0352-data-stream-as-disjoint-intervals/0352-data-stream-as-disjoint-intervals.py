class SummaryRanges:


    def __init__(self):
        self.h = defaultdict(int)
    

    def union(self,x,y):

        x1,y1 = self.find(x), self.find(y)


        if x1 != y1:
            if x1 > y1:
                self.h[y1] = x1
            else:
                self.h[x1] = y1
        

    def find(self,index):

        if self.h[index] != index:
            self.h[index] = self.find(self.h[index])
        
        return self.h[index]

    def addNum(self, value: int) -> None:
        self.h[value] = value
        if value -1 in self.h:
            self.union(value,value-1)
        if value +1 in self.h:
            self.union(value, value+1)
        

    def getIntervals(self) -> List[List[int]]:
        res = []
        
        end = -1
        ls = list(self.h.keys())
        ls.sort()
        start = ls[0]


        for key in ls:
            start = key
            if key > end:
                end = self.find(start)
                res.append([start,end])
                
        
        return res
    



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()