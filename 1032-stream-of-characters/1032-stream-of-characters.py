class Trie:
    
    def __init__(self, char):
        
        self.char = char
        self.adj = {}
        self.eow = False

class StreamChecker:

    def __init__(self, words: List[str]):
        
        self.tri = Trie('')
        self.mw = []
        for word in words:
            word = word[::-1]
            t = self.tri
            for c in word:
                if c in t.adj:
                    t = t.adj[c]
                else:
                    t.adj[c] = Trie(c)
                    t = t.adj[c]
            
            t.eow = True
            

    def query(self, letter: str) -> bool:
        
        self.mw.append(letter)
        found = False
        t = self.tri
        for i in range(len(self.mw)-1,-1,-1):
            char = self.mw[i]
            
            if char in t.adj:
                t = t.adj[char]
                if t.eow:
                    found = True
                    break
            else:
                break
        
        
        return found


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)