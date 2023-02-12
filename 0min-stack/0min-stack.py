class MinStack:

    def __init__(self):
        self.minStack = []
        #self.topStack = []
        self.allStack = []

    def push(self, val: int) -> None:
        if len(self.minStack) == 0 or self.minStack[-1] >= val:
            self.minStack.append(val)
        
        self.allStack.append(val)

    def pop(self) -> None:
        if self.top() != None and len(self.minStack) != 0 and self.top() == self.minStack[-1]:
        
            self.allStack.pop()
            self.minStack.pop()
        else:
            self.allStack.pop()

    def top(self) -> int:
        if len(self.allStack) == 0:
                return None
        else:
                return self.allStack[-1]

    def getMin(self) -> int:
      
        if len(self.minStack) == 0:
            return None
        else:
            return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()