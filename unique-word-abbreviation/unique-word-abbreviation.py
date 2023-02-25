class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.words = defaultdict(set)
        
        for word in dictionary:
            if len(word) <= 2:
                w = word[0] + word[-1]
                self.words[w].add(word)
            
            else:
                count = len(word) -2
                w = word[0] + str(count) + word[-1]
                self.words[w].add(word)
                
            

    def isUnique(self, word: str) -> bool:
        w = ''
        if len(word) <= 2:
            w = word[0] + word[-1]
            self.words[w].add(word)
            
        else:
            count = len(word) -2
            w = word[0] + str(count) + word[-1]
            
        if w in self.words:
            
            if word in self.words[w] and len(self.words[w]) == 1:
                return True
            return False
        else:
            return True
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)