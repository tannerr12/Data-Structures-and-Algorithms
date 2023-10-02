class T:
    def __init__(self, val):
        
        self.val = val
        self.adj = {}
        self.endCount = 0
        self.preCount = 1

class Trie:

    def __init__(self):
        self.tri = T('')
        

    def insert(self, word: str) -> None:
        t = self.tri
        for w in word:
            
            if w in t.adj:
                t = t.adj[w]
                t.preCount += 1
            else:
                t.adj[w] = T(w)
                t = t.adj[w]
        
        t.endCount += 1
            

    def countWordsEqualTo(self, word: str) -> int:
        t = self.tri
        
        for w in word:
            
            if w in t.adj:
                t = t.adj[w]
            else:
                return 0
        
        return max(0,t.endCount)
    
    def countWordsStartingWith(self, prefix: str) -> int:
        t = self.tri
        
        for w in prefix:
            
            if w in t.adj:
                t = t.adj[w]
            else:
                return 0
        
        return max(0,t.preCount)
            

    def erase(self, word: str) -> None:
        
        t = self.tri
        
        for w in word:
            
            if w in t.adj:
                t = t.adj[w]
                t.preCount -= 1
        
        t.endCount -= 1

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)