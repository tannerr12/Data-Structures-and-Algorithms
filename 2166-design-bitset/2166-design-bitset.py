class Bitset:

    def __init__(self, size: int):
        self.bit = 0
        self.size = size
        self.mask = (2 ** (size)) -1
        self.total = 0

    def fix(self, idx: int) -> None:
        idx = self.size - idx -1
        if self.bit & (1 << idx) == 0:
            self.bit |= (1 << idx)
            self.total +=1

    #fix
    def unfix(self, idx: int) -> None:
        idx = self.size - idx -1
        
        if self.bit & (1 << idx) > 0:
            self.copy = self.mask
            self.copy ^= (1 << idx)
            self.bit &= self.copy
            self.total -=1
       

    def flip(self) -> None:
        self.bit ^= self.mask
        self.total = self.size - self.total
    def all(self) -> bool:
        return self.bit == self.mask

    def one(self) -> bool:
        return self.bit != 0
    
    #logN fast bit counting/shifting by jumping to next active bit
    #O(1) sped up by counting bits as we go
    def count(self) -> int:
        """
        res = 0
        self.copy = self.bit
        while self.copy:
            self.copy &= self.copy -1
            res +=1
        return res
        """
        return self.total
    
    #O(N)
    #sped up using built in functions
    def toString(self) -> str:
        
        res= []
        """
        for i in range(self.size-1,-1,-1):
            if self.bit & (1 << i) > 0:
                res.append('1')
            else:
                res.append('0')
    
        """
        """
        return ''.join(res)
        """
        s = bin(self.bit).replace("0b", "")
        s2 = '0' * (self.size - len(s))
        return s2 + s
# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()