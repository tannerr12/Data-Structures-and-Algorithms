class Section:
    
    
    def __init__():
        
        
        
        self.s = set()
        
        self.arr = []


class TicTacToe:

    def __init__(self, n: int):
        self.size = n
        self.table = [[0 for i in range(n)] for j in range(n)]
        self.h = {}
        self.impossible = 0
        
        

    def move(self, row: int, col: int, player: int) -> int:
        
        self.table[row][col] = player
        self.impossible +=1
        
        if self.impossible * 2 < self.size:
            return 0
        #print(self.table)
        count = 0
        for r in range(self.size):
            if self.table[r][col] == player:
                count +=1
        
        if count == self.size:
            return player
        count = 0
        for c in range(self.size):
            if self.table[row][c] == player:
                count +=1
        
        #diagnals
        if count == self.size:
            return player
        count = 0
        for r in range(self.size):
            if self.table[r][r] == player:
                count +=1
        
        if count == self.size:
            return player
        count = 0
        rcount = 0
        for c in range(self.size-1,-1,-1):
            if self.table[rcount][c] == player:
                count +=1
            rcount +=1
        
        if count == self.size:
            return player
        count = 0
        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)