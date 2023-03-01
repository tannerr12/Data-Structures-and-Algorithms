# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.ns = nestedList
        self.stack = deque()
        self.idx = 0
        
        for i in range(len(self.ns)):
            if not self.ns[i].isInteger():
                self.dfs(0,self.ns[i].getList())
            else:
                self.stack.append(self.ns[i].getInteger())
        
        #print(self.stack)
            
        
    def dfs(self,i,n):
        
        
        if i > len(n):
            return
        
        for i in range(len(n)):
            
            if not n[i].isInteger():
                self.dfs(0,n[i].getList())
            else:
                self.stack.append(n[i].getInteger())
        
    
    def next(self) -> int:
        if self.hasNext:
            val = self.stack.popleft()
            return val
        return -1
    def hasNext(self) -> bool:
         return len(self.stack) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())