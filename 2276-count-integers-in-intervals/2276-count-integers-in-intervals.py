
from sortedcontainers import SortedList

class CountIntervals:

    #binary search and update range
    def __init__(self):
       
        self.sl = SortedList()
        self.total = 0

    def add(self, left: int, right: int) -> None:
        inf = float('inf')
        leftIndex =  self.sl.bisect_right((left,inf)) -1
        
        remove = []
        
        leftMost = left
        rightMost = right
        
        if leftIndex >= 0:
            L,R = self.sl[leftIndex]
            
            if L<= left <= right <=R:
                return
            if L <= left <= R <= right:
                leftMost = L
                remove.append((L,R))
            
        
        leftIndex +=1
        while leftIndex < len(self.sl):
            L,R = self.sl[leftIndex]
            
            if left <= L <= R <= right:
                remove.append((L,R))
                leftIndex +=1
            
            else:
                break
            
        
        if leftIndex < len(self.sl):
            L,R = self.sl[leftIndex]
            if left <= L <= right <= R:
                rightMost = R
                remove.append((L,R))
        
        for L,R in remove:
            self.total -= R-L +1
            self.sl.remove((L,R))
        
        self.sl.add((leftMost,rightMost))
        self.total += rightMost - leftMost + 1
        
            
            
    def count(self) -> int:
        return self.total


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()