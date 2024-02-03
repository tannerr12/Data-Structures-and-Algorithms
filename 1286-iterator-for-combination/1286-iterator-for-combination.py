class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        
        self.comb = list(itertools.combinations(characters, combinationLength))
        self.comb.sort()
        self.idx = 0

    def next(self) -> str:
        if self.hasNext():
            self.idx += 1
            return ''.join(self.comb[self.idx-1])
            
    def hasNext(self) -> bool:
        return self.idx < len(self.comb)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()