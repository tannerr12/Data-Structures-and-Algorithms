class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.q = deque()
        self.width = width
        self.height = height
        #self.grid = [[0 for i in range(width)] for j in range(height)]
        self.head = (0,0)
        self.eat = deque(food)
        self.score = 0
        self.tail = set()
        #print(self.grid)

    def move(self, direction: str) -> int:
       # print(direction)
        r,c = self.head
        thead = self.head
        check = False
        qr,qc = None,None
        if self.q:
            check = True
           # print(self.q)
          #  print(self.tail)
            
            qr,qc = self.q.popleft()
            
            self.tail.remove((qr,qc))
        
        
        if direction == 'R':
            c+=1
            self.head = (r,c)
        if direction == 'L':
            c -=1
            self.head = (r,c)
        if direction == 'U':
            r-=1
            self.head = (r,c)
        if direction == 'D':
            r+=1
            self.head = (r,c)
            
       # print(self.tail)
        #print(self.score)
        #print(self.q)
        if r >= self.height or r < 0 or c >= self.width or c < 0 or self.head in self.tail or self.head == (qr,qc):
            return -1
        if check:
            self.q.append(self.head)
            self.tail.add(self.head)
        if self.eat:
            re,ce = self.eat[0]
            if (r,c) == (re,ce):
                self.eat.popleft()
                self.score +=1
                if check:
                    self.q.appendleft((qr,qc))
                    self.tail.add((qr,qc))
                else:
                    self.q.append(self.head)
                    self.tail.add(self.head)
       # print(self.tail)
        return self.score
        
            
        

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)