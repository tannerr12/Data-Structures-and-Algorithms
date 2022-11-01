import random
class Solution:

    def __init__(self, m: int, n: int):
        self.exclude = set()
        self.width = n
        self.height = m
        self.size= m * n
        
        

    def flip(self) -> List[int]:
        
        c = randint(0,self.size-1)
        while c in self.exclude:
             c = randint(0,self.size-1)
       # print(c)
        self.exclude.add(c)
        
        x = 0
        y = 0
        if c > 0:
            x = c // self.width
            y = c % self.width
        
        res = [x, y]
       # print(res)
        return res
        
    def reset(self) -> None:
        self.exclude = set()
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()